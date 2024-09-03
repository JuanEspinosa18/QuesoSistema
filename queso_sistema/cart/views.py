from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.Carrito import Carrito
from inventory.models import Producto
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction
from sales.models import Pedido, DetallePedido

def carrito(request):
    carrito = request.session.get('carrito', {})
    total_carrito = sum(item['acumulado'] for item in carrito.values())
    return render(request, 'carrito.html', {'total_carrito': total_carrito, 'carrito': carrito})

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = request.session.get('carrito', {})

    id = str(producto_id)  # Asegúrate de que la clave esté en formato de cadena
    if id not in carrito:
        carrito[id] = {
            'nombre': producto.nombre,
            'cantidad': 1,
            'acumulado': producto.precio,
            'producto_id': producto_id
        }
    else:
        carrito[id]['cantidad'] += 1
        carrito[id]['acumulado'] += producto.precio

    request.session['carrito'] = carrito

    return redirect('carrito')  # Redirige al carrito o a otra página

@login_required
def procesar_pedido(request):
    carrito = request.session.get('carrito', {})

    if not carrito:
        return render(request, 'carrito.html', {'error': 'No hay productos en el carrito'})

    try:
        with transaction.atomic():  # Garantiza que todo se realice en una sola transacción
            # Crear el pedido
            pedido = Pedido.objects.create(
                cliente=request.user,
                subtotal=sum(item['acumulado'] for item in carrito.values())
            )

            # Crear los detalles del pedido
            for key, item in carrito.items():
                producto = Producto.objects.get(id=item['producto_id'])
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=item['cantidad'],
                    precio=producto.precio  # Se fija el precio al momento de realizar el pedido
                )

            # Limpiar el carrito después de crear el pedido
            request.session['carrito'] = {}

        # Agregar mensaje de éxito
        messages.success(request, '¡Pedido creado con éxito!')

        # Redirigir al carrito
        return redirect('carrito')

    except Exception as e:
        # Manejar errores si ocurre algún problema durante la transacción
        messages.error(request, 'Hubo un problema al procesar tu pedido.')
        return redirect('carrito')

@login_required
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(cliente=request.user).order_by('-fecha_pedido')
    return render(request, 'pedidosCliente.html', {'pedidos': pedidos})

def perfil_cliente(request):
    return render(request, 'perfilCliente.html', {
    })
#EJEMPLO ENVIO DE CORREO CLIENTE 
'''
def correo_pedido(request):
    if request.method == 'POST':
        subject = request.post['nombre']
        message = request.post['cantidad'] + " "+ request.post ['total_carrito']+ " "+request.post ['email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['jadu.jair@gmail.com']
        send_mail(subject,message,email_from,recipient_list)
        return render(request, 'gracias.html')
    return render(request, 'carrito.html')
    '''