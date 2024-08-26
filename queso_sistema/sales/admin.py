from django.contrib import admin
from .models import Factura, FacturaVenta, FacturaCompra, Pedido, PedidoProducto
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Registro de modelos
@admin.register(FacturaVenta)
class FacturaVentaAdmin(admin.ModelAdmin):
    pass

@admin.register(FacturaCompra)
class FacturaCompraAdmin(admin.ModelAdmin):
    pass

class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    extra = 1  # Número de formularios vacíos adicionales
    fields = ['producto', 'cantidad', 'precio']  # Solo los campos relevantes

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [PedidoProductoInline]
    list_display = ['id', 'usuario', 'fecha_pedido', 'subtotal']
    readonly_fields = ['subtotal']


@admin.register(PedidoProducto)
class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'producto', 'cantidad', 'precio']

@admin.register(Factura)
class FacturaAdmin(ImportExportModelAdmin):
    list_display = ['fecha_factura', 'subtotal', 'iva', 'total']
    readonly_fields = ['subtotal', 'iva', 'total']

class FacturaResource(resources.ModelResource):
    class Meta:
        model = Factura
        fields = ('id', 'fecha_factura')  # Asegúrate de incluir campos relevantes
