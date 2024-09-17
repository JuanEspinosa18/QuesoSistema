from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.productos, name='productos'),
    path('descontinuar_producto/<int:producto_id>/', views.descontinuar_producto, name='descontinuar_producto'),
    path('materia_prima/', views.materiaPrima, name='materia_prima'), 
]
