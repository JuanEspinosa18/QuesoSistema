from django.contrib import admin
from .models import Factura, FacturaVenta, FacturaCompra, FacturaDetalle, Pedido, PedidoProducto

# Inline para FacturaDetalle dentro de Factura
class FacturaDetalleInline(admin.TabularInline):
    model = FacturaDetalle
    extra = 1  # Número de formularios vacíos adicionales para añadir nuevos detalles

class FacturaAdmin(admin.ModelAdmin):
    inlines = [FacturaDetalleInline]
    readonly_fields = ['tipo_factura', 'subtotal', 'iva', 'total']
    list_display = ['id', 'tipo_factura', 'fecha_factura', 'subtotal', 'iva', 'total']
    list_filter = ['tipo_factura', 'fecha_factura']

class FacturaVentaAdmin(FacturaAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(tipo_factura='venta')

class FacturaCompraAdmin(FacturaAdmin):
    exclude = ['factura_compra_detalles']  
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(tipo_factura='compra')

# Inline para PedidoProducto dentro de Pedido
class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    extra = 1  # Número de formularios vacíos adicionales para añadir nuevos productos

class PedidoAdmin(admin.ModelAdmin):
    inlines = [PedidoProductoInline]
    readonly_fields = ['subtotal']
    list_display = ['id', 'usuario', 'fecha_pedido', 'subtotal']
    list_filter = ['fecha_pedido', 'usuario']

    def save_model(self, request, obj, form, change):
        # Guarda el objeto Pedido para asegurarte de que tenga una clave primaria
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        # Guarda primero los objetos relacionados de PedidoProducto
        super().save_related(request, form, formsets, change)

        # Ahora que los objetos relacionados están guardados, calcula y actualiza el subtotal
        obj = form.instance
        obj.subtotal = sum(item.precio * item.cantidad for item in obj.productos.all())
        obj.save()



# Registro de los modelos en el admin
admin.site.register(FacturaVenta, FacturaVentaAdmin)
admin.site.register(FacturaCompra, FacturaCompraAdmin)
admin.site.register(Pedido, PedidoAdmin)
