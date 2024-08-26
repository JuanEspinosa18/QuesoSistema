from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.DashInventario, name='inventario'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('materia_prima/', views.MateriaPrima, name='materia_prima'), 
    path('agregar_materiaPrima/', views.agregar_MateriaPrima, name='agregar_materia_prima'),
    path('eliminar_materiaPrima/<int:id>/', views.eliminar_MateriaPrima, name='eliminar_materia_prima'),
    path('editar_materiaPrima/<int:id>/', views.editar_MateriaPrima, name='editar_materia_prima'),
    path('stock_bajo_productos/', views.mostrar_stock_bajo_productos, name='stock_bajo_productos'),
    path('stock_bajo_materias_primas/', views.mostrar_stock_bajo_materias_primas, name='stock_bajo_materias_primas'),
]
