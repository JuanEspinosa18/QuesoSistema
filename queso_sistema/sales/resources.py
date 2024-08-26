from import_export import resources
from .models import Factura

class FacturaResource(resources.ModelResource):
    class Meta:
        model = Factura
        fields = ('id', 'pedido__usuario__email', 'fecha_factura', 'subtotal', 'iva', 'total')
        export_order = ('id', 'pedido__usuario__email', 'fecha_factura', 'subtotal', 'iva', 'total')
