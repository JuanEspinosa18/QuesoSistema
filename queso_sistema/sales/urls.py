from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.DashVentas, name='DashVentas'),
    path('pendientes/', views.pedidos_pendientes, name='pedidos_pendientes'),
    path('proceso/', views.pedidos_proceso, name='pedidos_proceso'),
    path('completados/', views.pedidos_completados, name='pedidos_completados'),
    path('cancelados/', views.pedidos_cancelados, name='pedidos_cancelados'),
    path('export_pedidos/', views.export_pedidos, name='export_pedidos'),
    path('consultar_pedido/<int:id>/', views.consultar_pedido, name='consultar_pedido'),
    path('editar_pedido_pendiente/<int:id>/', views.editar_pedido_pendiente, name='editar_pedido_pendiente'),
    path('editar_pedido_proceso/<int:id>/', views.editar_pedido_proceso, name='editar_pedido_proceso'),
    path('editar_pedido_completado/<int:id>/', views.editar_pedido_completado, name='editar_pedido_completado'),
    path('editar_pedido_cancelado/<int:id>/', views.editar_pedido_cancelado, name='editar_pedido_cancelado'),
    path('prueba/', views.prueba, name='prueba'),
    
]
