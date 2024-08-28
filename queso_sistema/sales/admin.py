from django.contrib import admin
from .models import Factura, FacturaVenta, FacturaCompra, Pedido, PedidoProducto, FacturaCompraDetalle
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class FacturaCompraDetalleInline(admin.TabularInline):
    model = FacturaCompraDetalle
    extra = 1
    fields = ('materia_prima', 'cantidad', 'precio')


# Admin para FacturaCompraDetalle
@admin.register(FacturaCompraDetalle)
class FacturaCompraDetalleAdmin(admin.ModelAdmin):
    list_display = ('factura_compra', 'materia_prima', 'cantidad', 'precio')
    fields = ('factura_compra', 'materia_prima', 'cantidad', 'precio')

# Admin para Factura
@admin.register(Factura)
class FacturaAdmin(ImportExportModelAdmin):
    list_display = ['tipo_factura', 'fecha_factura', 'subtotal', 'iva', 'total']
    fields = ['tipo_factura', 'fecha_factura', 'subtotal', 'iva', 'total']
    readonly_fields = ['subtotal', 'iva', 'total']

# Admin para FacturaVenta
@admin.register(FacturaVenta)
class FacturaVentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_factura', 'empleado', 'cliente', 'subtotal', 'iva', 'total']
    fields = ['tipo_factura', 'pedido', 'empleado', 'cliente', 'subtotal', 'iva', 'total']
    readonly_fields = ['subtotal', 'iva', 'total']
     # Agrega inlines aquí si tienes detalles de venta como en `FacturaCompra`


# Admin para FacturaCompra
@admin.register(FacturaCompra)
class FacturaCompraAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_factura', 'proveedor', 'empleado', 'subtotal', 'iva', 'total']
    fields = ['tipo_factura', 'proveedor', 'empleado', 'factura_compra_detalles', 'subtotal', 'iva', 'total']
    readonly_fields = ['subtotal', 'iva', 'total']
    inlines = [FacturaCompraDetalleInline]  # Agrega el inline aquí




# Admin para PedidoProducto (inline en PedidoAdmin)
class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    extra = 1
    fields = ['producto', 'cantidad', 'precio']

# Admin para Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [PedidoProductoInline]
    list_display = ['id', 'usuario', 'fecha_pedido', 'subtotal']
    readonly_fields = ['subtotal']

# Admin para PedidoProducto
@admin.register(PedidoProducto)
class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'producto', 'cantidad', 'precio']
