from django.shortcuts import render, redirect
from cart.Carrito import Carrito
from inventory.models import Producto
from django.core.mail import send_mail
from django.conf import settings

def carrito(request):
    productos = Producto.objects.all()
    carrito = Carrito(request)
    total_carrito = carrito.total_carrito()
    return render(request, "cart/carrito.html", {'productos': productos, 'total_carrito': total_carrito})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

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