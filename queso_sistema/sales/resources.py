from import_export import resources
from .models import Pedido, DetallePedido

""" class FacturaResource(resources.ModelResource):
    class Meta:
        model = Factura
        fields = ('id', 'fecha_factura', 'subtotal', 'iva', 'total')
        export_order = ('id', 'fecha_factura', 'subtotal', 'iva', 'total')

class FacturaVentaResource(resources.ModelResource):
    class Meta:
        model = FacturaVenta
        fields = ('id', 'pedido__usuario__email', 'fecha_factura', 'subtotal', 'iva', 'total')
        export_order = ('id', 'pedido__usuario__email', 'fecha_factura', 'subtotal', 'iva', 'total')

class FacturaCompraResource(resources.ModelResource):
    class Meta:
        model = FacturaCompra
        fields = ('id', 'proveedor__email', 'fecha_factura', 'subtotal', 'iva', 'total')
        export_order = ('id', 'proveedor__email', 'fecha_factura', 'subtotal', 'iva', 'total') """


