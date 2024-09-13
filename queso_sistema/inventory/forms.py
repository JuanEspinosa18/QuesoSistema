from django import forms
from .models import LoteProducto

class LoteProductoForm(forms.ModelForm):
    class Meta:
        model = LoteProducto
        fields = ['producto', 'cantidad_producto', 'fecha_produccion', 'fecha_vencimiento']
