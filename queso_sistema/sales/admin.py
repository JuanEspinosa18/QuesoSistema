from django.contrib import admin
from .models import FacturaVenta, FacturaCompra, FacturaDetalle
from .models import Pedido, PedidoProducto


class FacturaDetalleInline(admin.TabularInline):
    model = FacturaDetalle
    extra = 1
    fields = ('materia_prima', 'producto', 'cantidad', 'precio')
    readonly_fields = ('materia_prima', 'producto', 'cantidad', 'precio')

class FacturaVentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_factura', 'fecha_factura', 'subtotal', 'iva', 'total', 'empleado', 'cliente')
    inlines = [FacturaDetalleInline]

class FacturaCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_factura', 'fecha_factura', 'subtotal', 'iva', 'total', 'proveedor', 'empleado')
    inlines = [FacturaDetalleInline]

admin.site.register(FacturaVenta, FacturaVentaAdmin)
admin.site.register(FacturaCompra, FacturaCompraAdmin)

class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    extra = 1
    fields = ('producto', 'cantidad', 'precio')
    readonly_fields = ('producto', 'cantidad', 'precio')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_pedido', 'subtotal')
    inlines = [PedidoProductoInline]

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(FacturaDetalle)
