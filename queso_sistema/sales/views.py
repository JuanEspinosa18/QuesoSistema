import csv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from sales.models import Factura, FacturaVenta, FacturaCompra, CalificacionProducto, FacturaProducto
from users.models import CustomUser, UserProfile
from django.contrib import messages
from users.utils import is_employee

@login_required(login_url='/login')   
@user_passes_test(is_employee, login_url='/login/')
def DashVentas(request):
    facturas = Factura.objects.all()
    return render(request, 'DashVentas.html', {'facturas': facturas})

@login_required(login_url='/login')
@user_passes_test(is_employee, login_url='/login/')
def export_facturas(request):
    if request.method == "POST":
        file_format = request.POST.get('file_format')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="facturas_export.csv"'

        writer = csv.writer(response)
        writer.writerow(['name', 'fecha_factura', 'subtotal', 'iva', 'total'])

        facturas = Factura.objects.all().values_list('name', 'fecha_factura', 'subtotal', 'iva', 'total')
        for Factura in facturas:
            writer.writerow(Factura)

        return response

@login_required(login_url='/login/')
@user_passes_test(is_employee, login_url='/login/')
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

@login_required(login_url='/login/')
@user_passes_test(is_employee, login_url='/login/')
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

@login_required(login_url='/login')
@user_passes_test(is_employee, login_url='/login/')
def eliminar_factura(request, id):  # Añade 'id' como argumento
    factura_eliminar = get_object_or_404(Factura, id=id)  # Usa 'id' para obtener la factura
    if request.method == 'POST':
        factura_eliminar.delete()  # Elimina la factura
        return redirect('DashVentas')  # Redirige al usuario a la misma vista para evitar la reenvío del formulario
    else:
        # Si el método de la solicitud no es POST, muestra el formulario de confirmación
        return render(request, 'deletes_consulta/deleteFactura.html', {'factura': factura_eliminar})
    
@login_required(login_url='/login')
@user_passes_test(is_employee, login_url='/login/')   
def dashFacturaVenta(request):
    facturas_ventas = FacturaVenta.objects.all()
    facturas = Factura.objects.all()
    empleados = UserProfile.objects.filter(role__name='Empleado')
    clientes = UserProfile.objects.filter(role__name='Cliente')
    return render(request, 'sales/dashFacturaVenta.html', {
        'factura_ventas': facturas_ventas,
        'empleados': empleados,
        'clientes': clientes,
        'facturas': facturas,
    })


@login_required(login_url='/login')
@user_passes_test(is_employee, login_url='/login/')
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

@login_required(login_url='/login')
@user_passes_test(is_employee, login_url='/login/')
def agregar_factura_venta(request):
    if request.method == 'POST':
        factura_id = request.POST.get('factura')
        empleado_id = request.POST.get('empleado')
        cliente_id = request.POST.get('cliente')

        try:
            factura_instance = Factura.objects.get(id=factura_id)
            empleado_profile = UserProfile.objects.get(user_id=empleado_id)
            cliente_profile = UserProfile.objects.get(user_id=cliente_id)

            # Crear la instancia de FacturaVenta
            FacturaVenta.objects.create(
                factura=factura_instance,
                empleado=empleado_profile,
                cliente=cliente_profile
            )

            # Mensaje de éxito
            messages.success(request, 'La factura de venta se ha creado correctamente.')

            # Redirigir a una vista específica después de agregar la factura
            return redirect('factura_venta')

        except Factura.DoesNotExist:
            messages.error(request, 'La factura especificada no existe.')
        except UserProfile.DoesNotExist:
            messages.error(request, 'El empleado o cliente especificado no existe.')

    # Obtener las listas de facturas, empleados y clientes para el formulario
    facturas = Factura.objects.all()
    empleados = UserProfile.objects.filter(role__name='Empleado')
    clientes = UserProfile.objects.filter(role__name='Cliente')

    return render(request, 'dashFacturaVenta.html', {
        'facturas': facturas,
        'empleados': empleados,
        'clientes': clientes
    })


@login_required(login_url='/login')
@user_passes_test(is_employee, login_url='/login/')
def dashFacturaCompra(request):
    factura_compras = FacturaCompra.objects.all()
    facturas = Factura.objects.all()
    proveedores = UserProfile.objects.filter(role__name='Proveedor')
    empleados = UserProfile.objects.filter(role__name='Empleado')

    return render(request, 'sales/dashFacturaCompra.html', {
        'factura_compras': factura_compras,
        'facturas': facturas,
        'proveedores': proveedores,
        'empleados': empleados,
    })

    
@login_required(login_url='/login')
@user_passes_test(is_employee, login_url='/login/')
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

@login_required(login_url='/login')
@user_passes_test(is_employee, login_url='/login/')
def agregar_factura_compra(request):
    if request.method == 'POST':
        factura_id = request.POST.get('factura')
        proveedor_id = request.POST.get('proveedor')
        empleado_id = request.POST.get('empleado')

        try:
            factura_instance = Factura.objects.get(id=factura_id)
            proveedor_profile = UserProfile.objects.get(id=proveedor_id, role__name='Proveedor')
            empleado_profile = UserProfile.objects.get(id=empleado_id, role__name='Empleado')

            FacturaCompra.objects.create(
                factura=factura_instance,
                proveedor=proveedor_profile,
                empleado=empleado_profile
            )

            messages.success(request, 'La factura de compra se ha creado correctamente.')
            return redirect('factura_compra')

        except Factura.DoesNotExist:
            messages.error(request, 'La factura especificada no existe.')
        except UserProfile.DoesNotExist:
            messages.error(request, 'El proveedor o empleado especificado no existe.')

    facturas = Factura.objects.all()
    proveedores = UserProfile.objects.filter(role__name='Proveedor')
    empleados = UserProfile.objects.filter(role__name='Empleado')

    return render(request, 'sales/dashFacturaCompra.html', {
        'facturas': facturas,
        'proveedores': proveedores,
        'empleados': empleados
    })

@login_required(login_url='/login')
@user_passes_test(is_employee, login_url='/login/')   
def dashCalificacionProducto(request):
    calificacion_productos = CalificacionProducto.objects.all()
    return render(request, 'sales/dashCalificacionProducto.html', {'calificacion_productos': calificacion_productos})
