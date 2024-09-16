from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.Carrito import Carrito
from inventory.models import Producto
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.db import transaction
from sales.models import Pedido, DetallePedido
from django.contrib import messages
from .forms import ClienteProfileForm

@login_required
def carrito(request):
    carrito = request.session.get('carrito', {})
    total_carrito = sum(item['acumulado'] for item in carrito.values())
    pedido_id = request.GET.get('pedido_id')  # Obtén el pedido_id desde la URL si está presente
    return render(request, 'cart/carrito.html', {'total_carrito': total_carrito, 'pedido_id': pedido_id})

@login_required
def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

@login_required
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = request.session.get('carrito', {})

    id = str(producto_id) 
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

    # Añadir mensaje de éxito
    messages.success(request, f'{producto.nombre} ha sido agregado al carrito.')

    return redirect('catalogo')  # Redirige al catálogo o donde prefieras

def enviar_correo_pedido_cliente(pedido, detalles):
    try:
        asunto = f'Tu pedido #{pedido.id} ha sido creado'
        mensaje_html = render_to_string('emails/pedido_creado_cliente.html', {'pedido': pedido, 'detalles': detalles})
        mensaje_texto = f"Hola {pedido.cliente.primer_nombre}, tu pedido #{pedido.id} ha sido registrado con éxito. Pronto recibirás más actualizaciones."

        send_mail(
            asunto,
            mensaje_texto,
            settings.DEFAULT_FROM_EMAIL,
            [pedido.cliente.email],
            html_message=mensaje_html
        )
    except Exception as e:
        print(f'Error al enviar correo al cliente: {e}')

@login_required
def procesar_pedido(request):
    carrito = request.session.get('carrito', {})

    if not carrito:
        messages.warning(request, 'No hay productos en el carrito')
        return redirect('carrito')

    try:
        with transaction.atomic():
            # Crear el pedido
            pedido = Pedido.objects.create(
                cliente=request.user,
                subtotal=sum(item['acumulado'] for item in carrito.values())
            )

            # Crear los detalles del pedido
            detalles = []
            for key, item in carrito.items():
                producto = Producto.objects.get(id=item['producto_id'])
                detalle = DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=item['cantidad'],
                    precio=producto.precio
                )
                detalles.append(detalle)

            # Limpiar el carrito después de crear el pedido
            request.session['carrito'] = {}

            # Guardar el ID del pedido en la sesión
            request.session['last_order_id'] = pedido.id  # Solo aquí

            # Restablecer la bandera de notificación
            if 'notificacion_enviada' in request.session:
                del request.session['notificacion_enviada']

        # Intentar enviar el correo
        try:
            enviar_correo_pedido_admin(pedido, detalles)
            messages.success(request, '¡Pedido creado con éxito!')
            return redirect('carrito')
        except Exception as email_error:
            messages.warning(request, f'Pedido creado, pero hubo un problema al enviar el correo: {email_error}')
            return redirect('carrito')

    except Exception as e:
        messages.error(request, f'Hubo un problema al procesar tu pedido: {e}')
        return redirect('carrito')

@login_required
def activar_notificaciones_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, cliente=request.user)
    detalles = DetallePedido.objects.filter(pedido=pedido)  # Obtener los detalles del pedido
    pedido.notificaciones_activas = True  # Activar notificaciones
    pedido.save()

    # Enviar el correo para este pedido si no se ha hecho ya
    if 'notificacion_enviada' not in request.session:
        enviar_correo_pedido_cliente(pedido, detalles)
        # Marcar la notificación como enviada solo para este pedido
        request.session['notificacion_enviada'] = True
        
    request.session['notificaciones_activadas'] = True
    messages.success(request, 'Has activado las notificaciones para tu pedido.')
    return redirect('carrito')

def enviar_correo_pedido_admin(pedido, detalles):
    """
    Función para enviar un correo al administrador con los detalles del pedido.
    """
    subject = f'Nuevo Pedido #{pedido.id} - Cliente: {pedido.cliente.email}'
    message = f"Detalles del Pedido #{pedido.id}\n\n"
    
    for detalle in detalles:
        message += f"Producto: {detalle.producto.nombre}\n"
        message += f"Cantidad: {detalle.cantidad}\n"
        message += f"Precio Unitario: ${detalle.precio}\n"
        message += "----------------------\n"

    message += f"Subtotal: ${pedido.subtotal}\n"
    message += f"Cliente: {pedido.cliente.primer_nombre} ({pedido.cliente.email})\n"
    message += f"Fecha del pedido: {pedido.fecha_pedido}\n"

    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['soporte.quesosistema@gmail.com']  # Cambia a la dirección del administrador

    # Enviar el correo
    send_mail(subject, message, email_from, recipient_list)
   
@login_required
def limpiar_notificacion_flag(request):
    if 'notificacion_enviada' in request.session:
        del request.session['notificacion_enviada']  # Eliminar la bandera de sesión
    messages.info(request, 'Preferencias de notificación actualizadas.')
    return redirect('carrito')  # Redirigir al carrito

@login_required
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(cliente=request.user).order_by('-fecha_pedido')
    return render(request, 'cart/pedidosCliente.html', {'pedidos': pedidos})

@login_required
def cancelar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, cliente=request.user)

    if pedido.estado == 'pendiente':  
        pedido.estado = 'cancelado'
        pedido.save()
        messages.error(request, f'El pedido #{pedido.id} ha sido cancelado.')

    return redirect('mis_pedidos')  

@login_required
def perfil_cliente(request):
    if request.method == 'POST':
        form = ClienteProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado con éxito.')
            return redirect('perfil_cliente')
        else:
            print(form.errors)  # Esto imprimirá los errores del formulario en la consola
            messages.error(request, 'Por favor corrige los errores a continuación.')

    else:
        form = ClienteProfileForm(instance=request.user)

    return render(request, 'users/perfilCliente.html', {
        'form': form,
        'user': request.user,
    })