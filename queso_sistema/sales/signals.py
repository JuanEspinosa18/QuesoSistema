from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PedidoProducto
import logging
from decimal import Decimal

logger = logging.getLogger(__name__)

@receiver(post_save, sender=PedidoProducto)
def update_pedido_subtotal(sender, instance, **kwargs):
    logger.info(f'Post-save signal triggered for PedidoProducto: {instance}')
    pedido = instance.pedido
    pedido.subtotal = pedido.calcular_subtotal()
    pedido.save()

@receiver(post_delete, sender=PedidoProducto)
def update_pedido_subtotal_on_delete(sender, instance, **kwargs):
    logger.info(f'Post-delete signal triggered for PedidoProducto: {instance}')
    pedido = instance.pedido
    pedido.subtotal = pedido.calcular_subtotal()
    pedido.save()
