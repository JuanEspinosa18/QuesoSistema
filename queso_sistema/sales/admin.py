from django import forms
from django.contrib import admin
from .models import Pedido, DetallePedido

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = '__all__'

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    form = DetallePedidoForm
    extra = 1
    readonly_fields = ('precio',)  # El campo precio no debe ser editable

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_pedido', 'estado', 'subtotal')
    search_fields = ('cliente__email', 'estado')
    list_filter = ('estado', 'fecha_pedido')
    readonly_fields = ('subtotal',)
    inlines = [DetallePedidoInline]  # Muestra los detalles del pedido en línea

    def save_model(self, request, obj, form, change):
        # Actualiza el subtotal al guardar el pedido
        obj.actualizar_subtotal()
        super().save_model(request, obj, form, change)

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido)
