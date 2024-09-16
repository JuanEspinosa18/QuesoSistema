from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.productos, name='productos'),
    path('materia_prima/', views.materiaPrima, name='materia_prima'), 
]
