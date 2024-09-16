from django import forms
from .models import MateriaPrima, EntradaMateriaPrima
class MateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = MateriaPrima
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agregue un nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Agregue la descripción'}),
        }

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        max_length = 100
        if len(descripcion) > max_length:
            raise forms.ValidationError(f"La descripción no puede exceder los {max_length} caracteres.")
        return descripcion

class EntradaMateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = EntradaMateriaPrima
        fields = ['proveedor', 'materia_prima', 'cantidad', 'fecha_vencimiento', 'costo_total']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'materia_prima': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad', 'min': '0', 'max': '1000', 'step': '1'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'costo_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el costo total', 'min': '0', 'max': '10000000', 'step': '1000'}),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is not None and cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser mayor que cero.")
        return cantidad

    def clean_costo_total(self):
        costo_total = self.cleaned_data.get('costo_total')
        if costo_total is not None and costo_total <= 0.0:
            raise forms.ValidationError("El costo total debe ser mayor que cero.")
        return costo_total
