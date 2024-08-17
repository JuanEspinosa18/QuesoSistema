from django.contrib import admin
from .models import Factura, FacturaVenta, FacturaCompra, FacturaProducto, CalificacionProducto
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(FacturaVenta)
admin.site.register(FacturaCompra)
admin.site.register(FacturaProducto)
admin.site.register(CalificacionProducto)

@admin.register(Factura)
class VentaAdmin(ImportExportModelAdmin):
    list_display = ['fecha_factura'] 
    

class VentaResource(resources.ModelResource):
    class Meta:
        model = Factura
        fields = ('name')
        
