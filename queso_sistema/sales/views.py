from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from sales.models import Factura, FacturaVenta, FacturaCompra, CalificacionProducto, FacturaProducto
from django.contrib import messages
from import_export.formats.base_formats import XLSX
from .resources import FacturaResource
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.contrib.auth.models import Group
from users.views import group_required

@group_required('Empleados')   
def DashVentas(request):
    facturas = Factura.objects.all()
    return render(request, 'DashVentas.html', {'facturas': facturas})

@group_required('Empleados')
def export_facturas(request):
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
                p.drawString(100, y, f"{factura['name']} - {factura['fecha_factura']} - {factura['subtotal']}")
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

@group_required('Empleados')
def editar_factura(request, id):
    factura_editar = get_object_or_404(Factura, id=id)
    
    if request.method == 'POST':
        nombre = request.POST.get('name')
        fecha_factura = f"{request.POST.get('fecha_factura_0')} {request.POST.get('fecha_factura_1')}"
        subtotal = request.POST.get('subtotal')
        iva = request.POST.get('iva')
        total = request.POST.get('total')

        # Verifica que el total es correcto
        calculated_total = float(subtotal) + float(iva)
        if not total or float(total) != calculated_total:
            return render(request, 'edits/editarFactura.html', {
                'factura': factura_editar,
                'error': 'El total debe ser igual a la suma del subtotal más el IVA.'
            })

        # Actualiza los datos de la factura
        factura_editar.name = nombre
        factura_editar.fecha_factura = fecha_factura
        factura_editar.subtotal = subtotal
        factura_editar.iva = iva
        factura_editar.total = total
        factura_editar.save()

        return redirect('DashVentas')

    return render(request, 'edits/editarFactura.html', {'factura': factura_editar})

@group_required('Empleados')
def agregar_factura(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        fecha_factura = request.POST.get('fecha_factura')
        subtotal = request.POST.get('subtotal')
        iva = request.POST.get('iva')
        total = request.POST.get('total')
        
        errors = {}
        
        if not nombre:
            errors['nombre'] = 'El nombre es requerido.'
        if not fecha_factura:
            errors['fecha_factura'] = 'La fecha de la factura es requerida.'
        if not subtotal or float(subtotal) <= 0:
            errors['subtotal'] = 'El subtotal debe ser mayor que cero.'
        if not iva or float(iva) < 0:
            errors['iva'] = 'El IVA debe ser un valor positivo o cero.'
        if not total or float(total) <= 0:
            errors['total'] = 'El total debe ser mayor que cero.'
        
        if errors:
            return JsonResponse({'success': False, 'errors': errors})
        
        # Crear y guardar la nueva instancia de Factura si no hay errores
        factura_nueva = Factura(
            name=nombre, 
            fecha_factura=fecha_factura, 
            subtotal=subtotal, 
            iva=iva, 
            total=total
        )
        factura_nueva.save()
        
        return JsonResponse({'success': True})
    
    facturas = Factura.objects.all()
    return render(request, 'DashVentas.html', {'facturas': facturas})

@group_required('Empleados')
def eliminar_factura(request, id):  # Añade 'id' como argumento
    factura_eliminar = get_object_or_404(Factura, id=id)  # Usa 'id' para obtener la factura
    if request.method == 'POST':
        factura_eliminar.delete()  # Elimina la factura
        return redirect('DashVentas')  # Redirige al usuario a la misma vista para evitar la reenvío del formulario
    else:
        # Si el método de la solicitud no es POST, muestra el formulario de confirmación
        return render(request, 'deletes_consulta/deleteFactura.html', {'factura': factura_eliminar})
    
@group_required('Empleados')   
def dashFacturaVenta(request):
    facturas_ventas = FacturaVenta.objects.all()
    facturas = Factura.objects.all()
    empleados = Group.objects.get(name='Empleados').user_set.all()
    clientes = Group.objects.get(name='Clientes').user_set.all()
    return render(request, 'dashFacturaVenta.html', {
        'factura_ventas': facturas_ventas,
        'empleados': empleados,
        'clientes': clientes,
        'facturas': facturas,
    })

@group_required('Empleados')
def consultar_factura_venta(request, id):
    factura_instance = get_object_or_404(Factura, id=id)
    facturas_venta = FacturaVenta.objects.filter(factura=factura_instance)
    facturas_producto = FacturaProducto.objects.filter(factura=factura_instance)

    context = {
        'factura': factura_instance,
        'facturas_venta': facturas_venta,
        'facturas_producto': facturas_producto,
    }
    return render(request, 'deletes_consulta/consultarFacturaVenta.html', context)

@group_required('Empleados')
def agregar_factura_venta(request):
    if request.method == 'POST':
        factura_id = request.POST.get('factura')
        empleado_id = request.POST.get('empleado')
        cliente_id = request.POST.get('cliente')

        try:
            factura_instance = Factura.objects.get(id=factura_id)
            empleado = Group.objects.get(name='Empleado').user_set.get(id=empleado_id)
            cliente = Group.objects.get(name='Cliente').user_set.get(id=cliente_id)

            # Crear la instancia de FacturaVenta
            FacturaVenta.objects.create(
                factura=factura_instance,
                empleado=empleado,
                cliente=cliente
            )

            # Mensaje de éxito
            messages.success(request, 'La factura de venta se ha creado correctamente.')

            # Redirigir a una vista específica después de agregar la factura
            return redirect('factura_venta')

        except Factura.DoesNotExist:
            messages.error(request, 'La factura especificada no existe.')
        except Group.DoesNotExist:
            messages.error(request, 'El empleado o cliente especificado no existe.')

    # Obtener las listas de facturas, empleados y clientes para el formulario
    facturas = Factura.objects.all()
    empleados = Group.objects.get(name='Empleado').user_set.all()
    clientes = Group.objects.get(name='Cliente').user_set.all()

    return render(request, 'dashFacturaVenta.html', {
        'facturas': facturas,
        'empleados': empleados,
        'clientes': clientes
    })

@group_required('Empleados')
def dashFacturaCompra(request):
    factura_compras = FacturaCompra.objects.all()
    facturas = Factura.objects.all()
    proveedores = Group.objects.get(name='Proveedores').user_set.all()
    empleados = Group.objects.get(name='Empleados').user_set.all()

    return render(request, 'dashFacturaCompra.html', {
        'factura_compras': factura_compras,
        'facturas': facturas,
        'proveedores': proveedores,
        'empleados': empleados
    })

@group_required('Empleados')
def consultar_factura_compra(request, id):
    factura_instance = get_object_or_404(Factura, id=id)
    facturas_compra = FacturaCompra.objects.filter(factura=factura_instance)
    facturas_producto = FacturaProducto.objects.filter(factura=factura_instance)

    context = {
        'factura': factura_instance,
        'facturas_compra': facturas_compra,
        'facturas_producto': facturas_producto,
    }
    return render(request, 'deletes_consulta/consultarFacturaCompra.html', context)

@group_required('Empleados')
def agregar_factura_compra(request):
    if request.method == 'POST':
        factura_id = request.POST.get('factura')
        proveedor_id = request.POST.get('proveedor')
        empleado_id = request.POST.get('empleado')

        try:
            factura_instance = Factura.objects.get(id=factura_id)
            proveedor = Group.objects.get(name='Proveedor').user_set.get(id=proveedor_id)
            empleado = Group.objects.get(name='Empleado').user_set.get(id=empleado_id)

            # Crear la instancia de FacturaCompra
            FacturaCompra.objects.create(
                factura=factura_instance,
                proveedor=proveedor,
                empleado=empleado
            )

            # Mensaje de éxito
            messages.success(request, 'La factura de compra se ha creado correctamente.')

            # Redirigir a una vista específica después de agregar la factura
            return redirect('factura_compra')

        except Factura.DoesNotExist:
            messages.error(request, 'La factura especificada no existe.')
        except Group.DoesNotExist:
            messages.error(request, 'El proveedor o empleado especificado no existe.')

    # Obtener las listas de facturas, empleados y proveedores para el formulario
    facturas = Factura.objects.all()
    proveedores = Group.objects.get(name='Proveedor').user_set.all()
    empleados = Group.objects.get(name='Empleado').user_set.all()

    return render(request, 'dashFacturaCompra.html', {
        'facturas': facturas,
        'proveedores': proveedores,
        'empleados': empleados
    })

@group_required('Empleados')
def consultar_factura_producto(request, id):
    factura_instance = get_object_or_404(Factura, id=id)
    facturas_producto = FacturaProducto.objects.filter(factura=factura_instance)
    
    context = {
        'factura': factura_instance,
        'facturas_producto': facturas_producto
    }
    return render(request, 'deletes_consulta/consultarFacturaProducto.html', context)

@group_required('Empleados')
def agregar_factura_producto(request):
    if request.method == 'POST':
        factura_id = request.POST.get('factura')
        producto_id = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')

        try:
            factura_instance = Factura.objects.get(id=factura_id)
            producto = Producto.objects.get(id=producto_id)

            # Crear la instancia de FacturaProducto
            FacturaProducto.objects.create(
                factura=factura_instance,
                producto=producto,
                cantidad=cantidad
            )

            # Mensaje de éxito
            messages.success(request, 'El producto se ha agregado a la factura correctamente.')

            # Redirigir a una vista específica después de agregar el producto
            return redirect('factura_producto')

        except Factura.DoesNotExist:
            messages.error(request, 'La factura especificada no existe.')
        except Producto.DoesNotExist:
            messages.error(request, 'El producto especificado no existe.')

    # Obtener las listas de facturas y productos para el formulario
    facturas = Factura.objects.all()
    productos = Producto.objects.all()

    return render(request, 'dashFacturaProducto.html', {
        'facturas': facturas,
        'productos': productos
    })

@group_required('Empleados')   
def dashCalificacionProducto(request):
    calificacion_productos = CalificacionProducto.objects.all()
    return render(request, 'dashCalificacionProducto.html', {'calificacion_productos': calificacion_productos})