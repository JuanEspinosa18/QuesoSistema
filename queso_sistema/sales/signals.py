from django.db.models.signals import pre_save,post_save, post_delete
from django.dispatch import receiver
from .models import PedidoProducto, Factura, FacturaCompra, FacturaDetalle
import logging
from decimal import Decimal

logger = logging.getLogger(__name__)

""" @receiver(post_save, sender=PedidoProducto)
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
    pedido.save()  """

@receiver(post_save, sender=PedidoProducto)
def actualizar_subtotal_despues_de_guardar(sender, instance, **kwargs):
    instance.pedido.actualizar_subtotal()

@receiver(post_delete, sender=PedidoProducto)
def actualizar_subtotal_despues_de_eliminar(sender, instance, **kwargs):
    instance.pedido.actualizar_subtotal()
        
@receiver(post_save, sender=FacturaDetalle)
def actualizar_totales_despues_de_guardar(sender, instance, **kwargs):
    if instance.factura:  # Verifica si el detalle tiene una factura asociada
        factura_compra = instance.factura
        factura_compra.actualizar_totales()

@receiver(post_delete, sender=FacturaDetalle)
def actualizar_totales_despues_de_eliminar(sender, instance, **kwargs):
    if instance.factura:  # Verifica si el detalle tiene una factura asociada
        factura_compra = instance.factura
        factura_compra.actualizar_totales()
