from django.shortcuts import render
from django.http import JsonResponse
from users.views import group_required
from django.contrib import messages
from .models import Producto, LoteProducto, MateriaPrimaLote, MateriaPrima, EntradaMateriaPrima
from .forms import MateriaPrimaForm, EntradaMateriaPrimaForm

""" Productos """

@group_required('Empleados')
def productos(request):
    productos = Producto.objects.all()
    lotes_producto = LoteProducto.objects.all()
    return render(request, 'inventory/productos.html', {'productos': productos,'lotes_producto': lotes_producto,})

""" Materias Primas """

@group_required('Empleados')
def materiaPrima(request):
    materias_primas = MateriaPrima.objects.all()
    entrada_materia_prima = EntradaMateriaPrima.objects.all()
    materia_form = MateriaPrimaForm()
    entrada_form = EntradaMateriaPrimaForm()

    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'materia_prima':
            materia_form = MateriaPrimaForm(request.POST)
            if materia_form.is_valid():
                materia_form.save()
                messages.success(request, "Materia prima agregada exitosamente.")
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': materia_form.errors})

        elif form_type == 'entrada_materia_prima':
            entrada_form = EntradaMateriaPrimaForm(request.POST)
            if entrada_form.is_valid():
                entrada = entrada_form.save()
                    
                # Actualizar la cantidad disponible de la materia prima
                materia_prima = entrada.materia_prima
                materia_prima.stock += entrada.cantidad
                materia_prima.save()

                messages.success(request, "Entrada de materia prima registrada exitosamente.")
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': entrada_form.errors})

    return render(request, 'inventory/materiaPrima.html', {
        'materias_primas': materias_primas,
        'entrada_materia_prima': entrada_materia_prima,
        'materia_form': materia_form,
        'entrada_form': entrada_form,
    })





