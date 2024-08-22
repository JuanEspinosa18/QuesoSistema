from import_export import resources
from .models import Factura

class FacturaResource(resources.ModelResource):
    class Meta:
        model = Factura
        fields = ('id', 'name', 'fecha_factura', 'subtotal', 'iva', 'total')
        export_order = ('name', 'fecha_factura', 'subtotal', 'iva', 'total')
