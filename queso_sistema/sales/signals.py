from django.db.models.signals import pre_save,post_save, post_delete
from django.dispatch import receiver
from .models import PedidoProducto, Factura, FacturaCompra
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

        
@receiver(post_save, sender=Factura)
def update_factura_calculations(sender, instance, **kwargs):
    if instance.tipo_factura == 'compra' and isinstance(instance, FacturaCompra):
        subtotal = sum(detalle.precio * detalle.cantidad for detalle in instance.factura_compra_detalles.all())
        iva_rate = Decimal('0.12')
        iva = subtotal * iva_rate
        total = subtotal + iva

        # Evita un loop infinito
        if (instance.subtotal != subtotal or instance.iva != iva or instance.total != total):
            Factura.objects.filter(pk=instance.pk).update(subtotal=subtotal, iva=iva, total=total)