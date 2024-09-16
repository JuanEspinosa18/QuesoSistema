from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, MateriaPrima, LoteProducto
from users.views import group_required
from django.contrib import messages
from .forms import LoteProductoForm

""" Productos """

@group_required('Empleados')
def productos(request):
    productos = Producto.objects.all()
    lotes_producto = LoteProducto.objects.all()
    return render(request, 'inventory/productos.html', {'productos': productos,'lotes_producto': lotes_producto,})

@group_required('Empleados')
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        imagen = request.FILES.get('imagen')

        try:
            producto = Producto(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                imagen=imagen
            )
            producto.save()
            messages.success(request, "El producto ha sido agregado exitosamente.")
            return redirect('productos')
        except Exception as e:
            messages.error(request, f"Hubo un error al agregar el producto: {str(e)}")
            productos = Producto.objects.all()
            return render(request, 'inventory/productos.html', {
                'productos': productos,
            })
    return redirect('productos')

@group_required('Empleados')
def agregar_lote_producto(request):
    if request.method == 'POST':
        form = LoteProductoForm(request.POST)
        if form.is_valid():
            # Guardar el lote
            lote = form.save()

            # Actualizar el stock del producto
            producto = lote.producto
            producto.stock += lote.cantidad_producto
            producto.save()

            messages.success(request, "El lote de producto se ha agregado exitosamente y el stock ha sido actualizado.")
            return redirect('productos')
        else:
            messages.error(request, "Hubo un error al agregar el lote de producto. Por favor, revisa los datos.")
            productos = Producto.objects.all()
            lotes_producto = LoteProducto.objects.all()
            return render(request, 'inventory/productos.html', {
                'productos': productos,
                'lotes_producto': lotes_producto,
                'form': form,
            })
    return redirect('productos')

@group_required('Empleados')
def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    
    if request.method == 'POST':
        # Actualizar los campos del producto
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        
        if request.FILES.get('imagen'):
            producto.imagen = request.FILES.get('imagen')
        
        try:
            producto.save()
            messages.success(request, "El producto ha sido actualizado exitosamente.")
            return redirect('productos')
        except Exception as e:
            messages.error(request, f"Hubo un error al actualizar el producto: {str(e)}")
            productos = Producto.objects.all()
            return render(request, 'inventory/productos.html', {
                'productos': productos,
                'producto': producto,
            })
    else:
        return render(request, 'inventory/productos.html', {
            'producto': producto
        })

@group_required('Empleados')
def descontinuar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.descontinuado = True
    producto.save()
    messages.success(request, f"El producto {producto.nombre} ha sido descontinuado.")
    return redirect('productos')

""" Materias Primas """

@group_required('Empleados')
def Materia_Prima(request):
    materias_primas = MateriaPrima.objects.all()
    return render(request, 'inventory/materiaPrima.html', {'materias_primas': materias_primas})

    if request.method == 'POST':
        form = MateriaPrimaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Materia prima agregada exitosamente.")
            return redirect('materia_prima')
        else:
            messages.error(request, "Error al agregar materia prima. Por favor, revisa los datos.")
    return redirect('materia_prima')

""" Alertas """

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