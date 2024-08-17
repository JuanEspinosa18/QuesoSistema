from django.contrib import admin
from .models import materia_prima, Producto,orden_produccion 
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(materia_prima)
admin.site.register(Producto)


@admin.register(orden_produccion)
class OrdenAdmin(ImportExportModelAdmin):
    list_display = ['fecha_orden'] 

class OrdenResource(resources.ModelResource):
    class Meta:
        model = orden_produccion
        fields = ('cantidad')