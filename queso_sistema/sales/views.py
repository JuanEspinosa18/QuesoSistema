from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect,get_object_or_404
from sales.models import Pedido, DetallePedido
from .resources import PedidoResource 
from io import BytesIO
from reportlab.lib.pagesizes import letter
from django.conf import settings
from reportlab.pdfgen import canvas
from users.views import group_required
from django.core.mail import send_mail
from django.template.loader import render_to_string

@group_required('Empleados') 
def dashboardPedidos(request):
    # Obtener todos los pedidos
    pedidos = Pedido.objects.all() 

    # Contar pedidos por estado
    pedidos_pendientes = Pedido.objects.filter(estado='pendiente').count()
    pedidos_proceso = Pedido.objects.filter(estado='en_proceso').count()
    pedidos_completados = Pedido.objects.filter(estado='completado').count()
    pedidos_cancelados = Pedido.objects.filter(estado='cancelado').count()

    # Crear el contexto para la plantilla
    context = {
        'pedidos': pedidos,
        'pedidos_pendientes': pedidos_pendientes,
        'pedidos_proceso': pedidos_proceso,
        'pedidos_completados': pedidos_completados,
        'pedidos_cancelados': pedidos_cancelados,
    } 

    # Renderizar la plantilla con el contexto
    return render(request, 'sales/dashboardPedidos.html', context)

@group_required('Empleados') 
def export_pedidos(request):
    if request.method == 'POST':
        file_format = request.POST.get('file_format')
        resource = PedidoResource()
        dataset = resource.export()  # Exporta los datos en el formato tablib
        
        if file_format == 'xlsx':
            # Exportar como XLSX
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="pedidos_export.xlsx"'
            response.write(dataset.export('xlsx'))
            return response
        
        elif file_format == 'pdf':
            # Generar PDF utilizando ReportLab
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="pedidos_export.pdf"'
            
            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            
            # Agrega contenido al PDF
            p.drawString(100, 750, "Reporte de Pedidos")
            
            # Iteración sobre el dataset y agregar filas al PDF
            y = 700
            for pedido in dataset.dict:
                cliente = pedido['cliente']  # Ajusta según los campos en dataset
                fecha_pedido = pedido['fecha_pedido']
                estado = pedido['estado']
                subtotal = pedido['subtotal']
                p.drawString(100, y, f"{cliente} - {fecha_pedido} - {estado} - {subtotal}")
                y -= 20  # Ajustar la altura según sea necesario
            
            p.showPage()
            p.save()
            
            # Escribir el contenido del buffer en el response
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
        
        else:
            return HttpResponseBadRequest("Formato no soportado")
    else:
        return HttpResponseBadRequest("Método no permitido")

@group_required('Empleados')   
def pedidos_pendientes(request):
    pedidos = Pedido.objects.filter(estado='pendiente')
    pedidos_proceso = Pedido.objects.filter(estado='en_proceso').count()
    pedidos_completados = Pedido.objects.filter(estado='completado').count()
    pedidos_cancelados = Pedido.objects.filter(estado='cancelado').count()

    # Crear el contexto para la plantilla
    context = {
        'pedidos': pedidos,
        'pedidos_proceso': pedidos_proceso,
        'pedidos_completados': pedidos_completados,
        'pedidos_cancelados': pedidos_cancelados,
    } 
    return render(request, 'sales/DashPendientes.html', context)

@group_required('Empleados')
def editar_pedido_pendiente(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        # Procesar el formulario (actualizar el estado del pedido)
        nuevo_estado = request.POST.get('nuevo_estado')
        if nuevo_estado:
            pedido.estado = nuevo_estado
            pedido.save()

            # Redirigir a la misma página o a una página específica después de guardar
            return redirect('pedidos_pendientes')  # Cambia 'pedidos_pendientes' por el nombre de tu vista o URL

    # Si el formulario no se envía correctamente o el estado no está presente
    return HttpResponseBadRequest('No se pudo actualizar el pedido')

@group_required('Empleados')   
def pedidos_proceso(request):
    pedidos = Pedido.objects.filter(estado='en_proceso')
    pedidos_pendientes = Pedido.objects.filter(estado='pendiente').count()
    pedidos_completados = Pedido.objects.filter(estado='completado').count()
    pedidos_cancelados = Pedido.objects.filter(estado='cancelado').count()

    # Crear el contexto para la plantilla
    context = {
        'pedidos': pedidos,
        'pedidos_pendientes': pedidos_pendientes,
        'pedidos_completados': pedidos_completados,
        'pedidos_cancelados': pedidos_cancelados,
    } 
    return render(request, 'sales/DashEnProceso.html', context)

def enviar_correo_cambio_estado(pedido):
    subject = f"Tu pedido #{pedido.id} ha cambiado de estado"
    message = render_to_string('emails/cambio_estado.html', {
        'pedido': pedido,
        'nuevo_estado': pedido.get_estado_display(),
    })
    send_mail(subject, message, 'soporte.quesosistema@gmail.com', [pedido.cliente.email])

@group_required('Empleados')
def editar_pedido_proceso(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        # Procesar el formulario (actualizar el estado del pedido)
        nuevo_estado = request.POST.get('nuevo_estado')
        if nuevo_estado:
            pedido.estado = nuevo_estado
            pedido.save()

            # Redirigir a la misma página o a una página específica después de guardar
            return redirect('pedidos_proceso')  # Cambia 'pedidos_pendientes' por el nombre de tu vista o URL

    # Si el formulario no se envía correctamente o el estado no está presente
    return HttpResponseBadRequest('No se pudo actualizar el pedido')

@group_required('Empleados')   
def pedidos_completados(request):
    pedidos = Pedido.objects.filter(estado='completado')
    pedidos_pendientes = Pedido.objects.filter(estado='pendiente').count()
    pedidos_proceso = Pedido.objects.filter(estado='en_proceso').count()
    pedidos_cancelados = Pedido.objects.filter(estado='cancelado').count()

    # Crear el contexto para la plantilla
    context = {
        'pedidos': pedidos,
        'pedidos_pendientes': pedidos_pendientes,
        'pedidos_proceso': pedidos_proceso,
        'pedidos_cancelados': pedidos_cancelados,
    } 
    return render(request, 'sales/DashCompletados.html', context)

@group_required('Empleados')
def editar_pedido_completado(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        # Procesar el formulario (actualizar el estado del pedido)
        nuevo_estado = request.POST.get('nuevo_estado')
        if nuevo_estado:
            pedido.estado = nuevo_estado
            pedido.save()

            # Redirigir a la misma página o a una página específica después de guardar
            return redirect('pedidos_completados')  # Cambia 'pedidos_pendientes' por el nombre de tu vista o URL

    # Si el formulario no se envía correctamente o el estado no está presente
    return HttpResponseBadRequest('No se pudo actualizar el pedido')

@group_required('Empleados')   
def pedidos_cancelados(request):
    pedidos = Pedido.objects.filter(estado='cancelado')
    pedidos_pendientes = Pedido.objects.filter(estado='pendiente').count()
    pedidos_proceso = Pedido.objects.filter(estado='en_proceso').count()
    pedidos_completados = Pedido.objects.filter(estado='completado').count()

    # Crear el contexto para la plantilla
    context = {
        'pedidos': pedidos,
        'pedidos_pendientes': pedidos_pendientes,
        'pedidos_proceso': pedidos_proceso,
        'pedidos_completados': pedidos_completados,
    } 
    return render(request, 'sales/dashCancelados.html', context)

@group_required('Empleados')
def editar_pedido_cancelado(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        # Procesar el formulario (actualizar el estado del pedido)
        nuevo_estado = request.POST.get('nuevo_estado')
        if nuevo_estado:
            pedido.estado = nuevo_estado
            pedido.save()

            # Redirigir a la misma página o a una página específica después de guardar
            return redirect('pedidos_cancelados')  # Cambia 'pedidos_pendientes' por el nombre de tu vista o URL

    # Si el formulario no se envía correctamente o el estado no está presente
    return HttpResponseBadRequest('No se pudo actualizar el pedido')

def consultar_pedido(request,id):
    pedido = get_object_or_404(Pedido, id=id)
    detalles_pedido = DetallePedido.objects.filter(pedido=pedido)
    
    return render(request, 'sales/consultas/consultar_pedido.html', {'pedido': pedido, 'detalles_pedido': detalles_pedido})