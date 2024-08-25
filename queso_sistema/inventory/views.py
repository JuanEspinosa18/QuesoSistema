from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from users.utils import is_employee
from .models import Producto, materia_prima
from django.contrib import messages
from django.http import JsonResponse
from users.views import group_required

@group_required('Empleados')
def DashInventario(request):
    productos = Producto.objects.all()
    return render(request, 'DashInventario.html', {'productos': productos})

@group_required('Empleados')
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        valor = request.POST.get('valor')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        cantidad_existente = request.POST.get('cantidad_existente')
        imagen = request.FILES.get('imagen')
        
        errors = {}
        if not nombre:
            errors['nombre'] = 'El nombre es requerido.'
        if not descripcion:
            errors['descripcion'] = 'La descripción es requerida.'
        if not valor or float(valor) <= 0:
            errors['valor'] = 'El valor debe ser mayor que cero.'
        if not fecha_vencimiento:
            errors['fecha_vencimiento'] = 'La fecha de vencimiento es requerida.'
        if not cantidad_existente or int(cantidad_existente) <= 0:
            errors['cantidad_existente'] = 'La cantidad existente debe ser mayor que cero.'
        if not imagen:
            errors['imagen'] = 'Debe seleccionar una imagen.'
        
        if errors:
            return JsonResponse({'success': False, 'errors': errors})
        else:
            # Guardar el producto
            producto_nuevo = Producto(
                nombre=nombre, 
                descripcion=descripcion, 
                valor=valor, 
                fecha_vencimiento=fecha_vencimiento, 
                cantidad_existente=cantidad_existente,
                imagen=imagen
            )
            producto_nuevo.save()
            return JsonResponse({'success': True})
    
    productos = Producto.objects.all()
    return render(request, 'DashInventario.html', {'productos': productos})

@group_required('Empleados')
def eliminar_producto(request, id):  
    eliminar_producto = get_object_or_404(Producto, id=id)  
    if request.method == 'POST':
        eliminar_producto.delete()  
        return redirect('inventario')  
    else:
        return render(request, 'deletes_edit/deleteProducto.html', {'producto': eliminar_producto})
    
@group_required('Empleados')
def editar_producto(request, id):
    factura_producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        # Procesa el formulario enviado para editar el producto
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        valor = request.POST.get('valor')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        cantidad_existente = request.POST.get('cantidad_existente')
        imagen = request.FILES.get('imagen')
        
        # Actualiza los datos del producto con los valores enviados en el formulario
        factura_producto.nombre = nombre
        factura_producto.descripcion = descripcion
        factura_producto.valor = valor
        factura_producto.fecha_vencimiento = fecha_vencimiento
        factura_producto.cantidad_existente = cantidad_existente
        
        if imagen:
            factura_producto.imagen = imagen
        
        factura_producto.save()
        
        # Redirige después de editar
        return redirect('inventario')
    
    return render(request, 'deletes_edit/editarProducto.html', {'Producto': factura_producto})

@group_required('Empleados')
def MateriaPrima(request):
    materias_primas = materia_prima.objects.all()
    return render(request, 'materiaPrima.html', {'materias_primas': materias_primas})

@group_required('Empleados')
def agregar_materia_prima(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        cantidad = request.POST.get('cantidad')

        errors = {}
        if not nombre:
            errors['nombre'] = 'El nombre es requerido.'
        if not descripcion:
            errors['descripcion'] = 'La descripción es requerida.'
        if not fecha_vencimiento:
            errors['fecha_vencimiento'] = 'La fecha de vencimiento es requerida.'
        if not cantidad or int(cantidad) <= 0:
            errors['cantidad'] = 'La cantidad debe ser mayor que cero.'

        if errors:
            return JsonResponse({'success': False, 'errors': errors})
        else:
            materia_nueva = materia_prima(
                name=nombre,
                descripcion=descripcion,
                fecha_ven=fecha_vencimiento,
                cantidad=cantidad
            )
            materia_nueva.save()
            return JsonResponse({'success': True})
    
    materias_primas = materia_prima.objects.all()
    return render(request, 'materiaPrima.html', {'materias_primas': materias_primas})

@group_required('Empleados')
def eliminar_materia_prima(request, id):
    eliminar_materia = get_object_or_404(materia_prima, id=id)
    if request.method == 'POST':
        eliminar_materia.delete()
        return redirect('materia_prima')
    return render(request, 'deletes_edit/deleteMateriaPrima.html', {'materia_prima': eliminar_materia})

@group_required('Empleados')
def editar_materia_prima(request, id):
    editar_materia = get_object_or_404(materia_prima, id=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        cantidad = request.POST.get('cantidad')

        editar_materia.name = nombre
        editar_materia.descripcion = descripcion
        editar_materia.fecha_ven = fecha_vencimiento
        editar_materia.cantidad = cantidad

        editar_materia.save()
        return redirect('materia_prima')

    return render(request, 'deletes_edit/editarMateriaPrima.html', {'materia_prima': editar_materia})

@group_required('Empleados')
def mostrar_stock_bajo_productos(request):
    productos_bajo_stock = Producto.objects.filter(cantidad_existente__lt=10)
    context = {
        'productos': productos_bajo_stock,
    }
    return render(request, 'stock_bajo_productos.html', context)

@group_required('Empleados')
def mostrar_stock_bajo_materias_primas(request):
    materias_primas_bajo_stock = materia_prima.objects.filter(cantidad__lt=10)
    context = {
        'materias_primas': materias_primas_bajo_stock,
    }
    return render(request, 'stock_bajo_materias_primas.html', context)