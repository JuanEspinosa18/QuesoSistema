from django.contrib import admin
from .models import Factura, FacturaVenta, FacturaCompra, Pedido, PedidoProducto, FacturaCompraDetalle
from import_export.admin import ImportExportModelAdmin

# Inline Admin para FacturaCompraDetalle
class FacturaCompraDetalleInline(admin.TabularInline):
    model = FacturaCompraDetalle
    extra = 1
    fields = ('materia_prima', 'cantidad', 'precio')

# Inline Admin para FacturaVenta (si tiene detalles específicos para mostrar)
class FacturaVentaInline(admin.TabularInline):
    model = FacturaVenta
    extra = 1
    fields = ('empleado', 'cliente', 'subtotal', 'iva', 'total')

# Admin para Factura
class FacturaAdmin(admin.ModelAdmin):
    model = Factura
    list_display = ['fecha_factura', 'subtotal', 'iva', 'total']
    list_filter = ['tipo_factura']
    readonly_fields = ['fecha_factura', 'subtotal', 'iva', 'total']  # Fecha no editable
    ordering = ['fecha_factura']

    def get_inlines(self, request, obj=None):
        if obj and obj.tipo_factura == 'compra':
            return [FacturaCompraDetalleInline]
        elif obj and obj.tipo_factura == 'venta':
            return [FacturaVentaInline]
        return []

    def get_fieldsets(self, request, obj=None):
        if obj:
            if obj.tipo_factura == 'compra':
                return [
                    (None, {'fields': ['fecha_factura', 'subtotal', 'iva', 'total']}),
                    ('Detalles de Compra', {'fields': ['factura_compra_detalles']}),
                ]
            elif obj.tipo_factura == 'venta':
                return [
                    (None, {'fields': ['fecha_factura', 'subtotal', 'iva', 'total']}),
                    ('Detalles de Venta', {'fields': ['empleado', 'cliente', 'pedido']}),
                ]
        return [
            (None, {'fields': ['subtotal', 'iva', 'total']}),
        ]

# Registro del admin para Factura
admin.site.register(Factura, FacturaAdmin)

# Admin para FacturaVenta
@admin.register(FacturaVenta)
class FacturaVentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_factura', 'empleado', 'cliente', 'subtotal', 'iva', 'total']
    fields = ['tipo_factura', 'pedido', 'empleado', 'cliente', 'subtotal', 'iva', 'total']
    readonly_fields = ['fecha_factura', 'subtotal', 'iva', 'total']

# Admin para FacturaCompra
@admin.register(FacturaCompra)
class FacturaCompraAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_factura', 'proveedor', 'empleado', 'subtotal', 'iva', 'total']
    fields = ['tipo_factura', 'proveedor', 'empleado', 'factura_compra_detalles', 'subtotal', 'iva', 'total']
    readonly_fields = ['fecha_factura', 'subtotal', 'iva', 'total']
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
