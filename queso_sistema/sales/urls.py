from django.urls import path
from . import views

urlpatterns = [
    path('facturas/', views.DashVentas, name='DashVentas'),
    path('export_facturas/', views.export_facturas, name='export_facturas'),
    path('agregar_factura/', views.agregar_factura, name='agregar_factura'),
    path('eliminar_factura/<int:id>/', views.eliminar_factura, name='eliminar_factura'),
    path('editar_factura/<int:id>/', views.editar_factura, name='editar_factura'),
    path('factura_venta/', views.dashFacturaVenta, name='factura_venta'),
    path('consultar_factura_venta/<int:id>/', views.consultar_factura_venta, name='consultar_factura_venta'),
    path('agregar_factura_venta/', views.agregar_factura_venta, name='agregar_factura_venta'),
    path('factura_compra/', views.dashFacturaCompra, name='factura_compra'),
    path('consultar_factura_compra/<int:id>/', views.consultar_factura_compra, name='consultar_factura_compra'),
    path('agregar_factura_compra/', views.agregar_factura_compra, name='agregar_factura_compra'),     
    path('calificacion/', views.dashCalificacionProducto, name='calificacion'),
]

