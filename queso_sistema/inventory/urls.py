from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.productos, name='productos'),
    path('descontinuar_producto/<int:producto_id>/', views.descontinuar_producto, name='descontinuar_producto'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_lote_producto/', views.agregar_lote_producto, name='agregar_lote_producto'),
    path('materia_prima/', views.Materia_Prima, name='materia_prima'), 
    path('stock_bajo_productos/', views.mostrar_stock_bajo_productos, name='stock_bajo_productos'),
    path('stock_bajo_materias_primas/', views.mostrar_stock_bajo_materias_primas, name='stock_bajo_materias_primas'),
]
