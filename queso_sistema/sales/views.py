from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from sales.models import Pedido, DetallePedido
from django.contrib import messages
from import_export.formats.base_formats import XLSX
#from .resources import FacturaResource
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.contrib.auth.models import Group
from users.views import group_required
from inventory.models import Producto

@group_required('Empleados')   
def DashVentas(request):
    pedidos = Pedido.objects.all()
    return render(request, 'DashVentas.html', {'pedidos': pedidos})

""" @group_required('Empleados')
def export_facturas(request):
    if request.method == 'POST':
        file_format = request.POST.get('file_format')
        resource = FacturaResource()
        
        # Exportar los datos en el formato tablib
        dataset = resource.export()
        
        if file_format == 'xlsx':
            # Exportar como XLSX
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="facturas_export.xlsx"'
            response.write(dataset.xlsx)
            return response
        
        elif file_format == 'pdf':
            # Generar PDF utilizando ReportLab
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="facturas_export.pdf"'
            
            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            
            # Agrega contenido al PDF
            p.drawString(100, 750, "Reporte de Facturas")
            
            # Iteracion sobre el dataset y agregar filas al PDF
            y = 700
            for factura in dataset.dict:
                # Asegúrate de que los datos sean accesibles de la forma correcta
                email = factura['pedido__usuario__email']
                fecha_factura = factura['fecha_factura']
                subtotal = factura['subtotal']
                iva = factura['iva']
                total = factura['total']
                p.drawString(100, y, f"{email} - {fecha_factura} - {subtotal} - {iva} - {total}")
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
    if request.method == 'POST':
        file_format = request.POST.get('file_format')
        resource = FacturaResource()
        dataset = resource.export()  # Exporta los datos en el formato tablib
        
        if file_format == 'xlsx':
            # Exportar como XLSX
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="facturas_export.xlsx"'
            response.write(dataset.export('xlsx'))
            return response
        
        elif file_format == 'pdf':
            # Generar PDF utilizando ReportLab
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="facturas_export.pdf"'
            
            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            
            # Agrega contenido al PDF
            p.drawString(100, 750, "Reporte de Facturas")
            
            # Iteracion sobre el dataset y agregar filas al PDF
            y = 700
            for factura in dataset.dict:
                p.drawString(100, y, f"{factura.pedido.usuario ['email']} - {factura['fecha_factura']} - {factura['subtotal']}")
                y -= 20  # Ajustar la altura según sea necesario
            
            p.showPage()
            p.save()
            
            # Escribir el contenido del buffer en el response
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
        
        else:
            return HttpResponseBadRequest("Formato no soportado") """
