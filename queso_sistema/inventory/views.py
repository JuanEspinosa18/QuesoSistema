from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, MateriaPrima, LoteProducto, MateriaPrimaLote
from django.http import JsonResponse
from users.views import group_required
from django.contrib import messages
from .forms import LoteProductoForm

@group_required('Empleados')
def productos(request):
    productos = Producto.objects.all()
    lotes_producto = LoteProducto.objects.all()
    
    return render(request, 'inventory/productos.html', {'productos': productos,'lotes_producto': lotes_producto,})

@group_required('Empleados')
def agregar_lote_producto(request):
    if request.method == 'POST':
        form = LoteProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El lote de producto se ha agregado exitosamente.")
            return redirect('productos')
        else:
            messages.error(request, "Hubo un error al agregar el lote de producto. Por favor, revisa los datos.")
            productos = Producto.objects.all()
            lotes_producto = LoteProducto.objects.all()
            return render(request, 'inventory/productos.html', {
                'productos': productos,
                'lotes_producto': lotes_producto,
                'form': form,  # Pasa el formulario con errores
            })
    return redirect('productos')

@group_required('Empleados')
def Materia_Prima(request):
    materias_primas = MateriaPrima.objects.all()
    return render(request, 'inventory/materiaPrima.html', {'materias_primas': materias_primas})

@group_required('Empleados')
def mostrar_stock_bajo_productos(request):
    productos_bajo_stock = Producto.objects.filter(stock__lt=10)
    context = {
        'productos': productos_bajo_stock,
    }
    return render(request, 'inventory/stock_bajo_productos.html', context)

@group_required('Empleados')
def mostrar_stock_bajo_materias_primas(request):
    materias_primas_bajo_stock = MateriaPrima.objects.filter(cantidad__lt=10)
    context = {
        'materias_primas': materias_primas_bajo_stock,
    }
    return render(request, 'inventory/stock_bajo_materias_primas.html', context)