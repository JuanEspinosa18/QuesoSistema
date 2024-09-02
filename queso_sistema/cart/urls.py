
from django.urls import path

from cart.views import carrito, eliminar_producto, restar_producto, limpiar_carrito, agregar_al_carrito, procesar_pedido, mis_pedidos

urlpatterns = [
    path('carrito/', carrito, name="carrito"),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='Add'),  # Mantén esta o la de abajo
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('procesar_pedido/', procesar_pedido, name='procesar_pedido'),
    path('mis-pedidos/', mis_pedidos, name='mis_pedidos'),
]

