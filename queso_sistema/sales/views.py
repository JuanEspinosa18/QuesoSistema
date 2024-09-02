from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from sales.models import Pedido, DetallePedido
from django.contrib import messages
from import_export.formats.base_formats import XLSX
from .resources import PedidoResource 
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.contrib.auth.models import Group
from users.views import group_required

@user_passes_test(lambda u: u.groups.filter(name='Empleados').exists())
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
def DashVentas(request):
    pedidos = Pedido.objects.all()
    return render(request, 'DashVentas.html', {'pedidos': pedidos})

@group_required('Empleados')   
def pedidos_pendientes(request):
    pedidos = Pedido.objects.filter(estado='pendiente')
    return render(request, 'DashPendientes.html', {'pedidos': pedidos})

@group_required('Empleados')
def editar_pedido_pendiente(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        # Procesar el formulario(actualizar el estado del pedido)
        nuevo_estado = request.POST.get('nuevo_estado')
        pedido.estado = nuevo_estado
        pedido.save()
        if request.is_ajax():
            data = {
                'estado': pedido.get_estado_display(),
            }
            return JsonResponse(data)

    return render(request, 'DashPendientes.html', {'pedido': pedido})

@group_required('Empleados')   
def pedidos_proceso(request):
    pedidos = Pedido.objects.filter(estado='en_proceso')
    return render(request, 'DashEnProceso.html', {'pedidos': pedidos})

@group_required('Empleados')
def editar_pedido_proceso(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        # Procesar el formulario(actualizar el estado del pedido)
        nuevo_estado = request.POST.get('nuevo_estado')
        pedido.estado = nuevo_estado
        pedido.save()
        if request.is_ajax():
            data = {
                'estado': pedido.get_estado_display(),
            }
            return JsonResponse(data)

    return render(request, 'DashEnProceso.html', {'pedido': pedido})

@group_required('Empleados')   
def pedidos_completados(request):
    pedidos = Pedido.objects.filter(estado='completado')
    return render(request, 'DashCompletados.html', {'pedidos': pedidos})

@group_required('Empleados')
def editar_pedido_completado(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        # Procesar el formulario(actualizar el estado del pedido)
        nuevo_estado = request.POST.get('nuevo_estado')
        pedido.estado = nuevo_estado
        pedido.save()
        if request.is_ajax():
            data = {
                'estado': pedido.get_estado_display(),
            }
            return JsonResponse(data)

    return render(request, 'DashCompletados.html', {'pedido': pedido})

@group_required('Empleados')   
def pedidos_cancelados(request):
    pedidos = Pedido.objects.filter(estado='cancelado')
    return render(request, 'dashCancelados.html', {'pedidos': pedidos})

@group_required('Empleados')
def editar_pedido_cancelado(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == 'POST':
        # Procesar el formulario (actualizar el estado del pedido)
        nuevo_estado = request.POST.get('nuevo_estado')
        pedido.estado = nuevo_estado
        pedido.save()
        if request.is_ajax():
            data = {
                'estado': pedido.get_estado_display(),
            }
            return JsonResponse(data)
        

    return render(request, 'dashCancelados.html', {'pedido': pedido})

def consultar_pedido(request,id):
    pedido = get_object_or_404(Pedido, id=id)
    detalles_pedido = DetallePedido.objects.filter(pedido=pedido)
    
    return render(request, 'consultas/consultar_pedido.html', {'pedido': pedido, 'detalles_pedido': detalles_pedido})

