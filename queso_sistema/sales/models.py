from django.conf import settings
from django.db import models
from decimal import Decimal
from users.models import Proveedor
from inventory.models import MateriaPrima, Producto

class Factura(models.Model):
    TIPO_FACTURA_CHOICES = [
        ('venta', 'Venta'),
        ('compra', 'Compra'),
    ]
    tipo_factura = models.CharField(max_length=10, choices=TIPO_FACTURA_CHOICES)
    fecha_factura = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de factura')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Subtotal', default=Decimal('0.00'))
    iva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='IVA', default=Decimal('0.00'))
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total', default=Decimal('0.00'))

    def __str__(self):
        return f"Factura #{self.id} - {self.get_tipo_factura_display()} - Total: {self.total}"

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        db_table = 'factura'
        ordering = ['id']


class FacturaVenta(Factura):
    pedido = models.OneToOneField('Pedido', on_delete=models.CASCADE, related_name='factura', null=True, blank=True)
    empleado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ventas_empleado', limit_choices_to={'groups__name': 'Empleados'})
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ventas_cliente', limit_choices_to={'groups__name': 'Clientes'})

    def save(self, *args, **kwargs):
        self.tipo_factura = 'venta'  # Establece el tipo de factura como "venta"
        self.subtotal = sum(item.precio * item.cantidad for item in self.pedido.productos.all())
        self.iva = self.subtotal * Decimal('0.19')
        self.total = self.subtotal + self.iva
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Factura de Venta'
        verbose_name_plural = 'Facturas de Venta'
        db_table = 'factura_venta'
        ordering = ['id']


class FacturaCompra(Factura):
    proveedor = models.ForeignKey(
        Proveedor, 
        on_delete=models.CASCADE,
        related_name='compras_proveedor'
    )
    empleado = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='compras_empleado',
        limit_choices_to={'groups__name': 'Empleados'}
    )
    factura_compra_detalles = models.ManyToManyField('FacturaDetalle', related_name='facturas', blank=True)

    def save(self, *args, **kwargs):
        # Solo actualiza tipo_factura si es una nueva instancia
        if not self.pk:
            self.tipo_factura = 'compra'
        super().save(*args, **kwargs)

    def actualizar_totales(self):
        # No redefinir subtotal, iva, total aquí si ya están en Factura
        self.subtotal = sum(item.precio * item.cantidad for item in self.factura_compra_detalles.all())
        self.iva = self.subtotal * Decimal('0.19')
        self.total = self.subtotal + self.iva
        self.save(update_fields=['subtotal', 'iva', 'total'])


class FacturaDetalle(models.Model):
    factura = models.ForeignKey('Factura', on_delete=models.CASCADE, related_name='detalles', null=True, blank=True)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.materia_prima:
            if not self.pk:
                if self.materia_prima.cantidad >= self.cantidad:
                    self.materia_prima.cantidad -= self.cantidad
                    self.materia_prima.save()
                else:
                    raise ValueError(f"No hay suficiente stock de {self.materia_prima.nombre} para realizar la compra.")
            else:
                original = FacturaDetalle.objects.get(pk=self.pk)
                diferencia_cantidad = self.cantidad - original.cantidad
                if diferencia_cantidad > 0:
                    if self.materia_prima.cantidad >= diferencia_cantidad:
                        self.materia_prima.cantidad -= diferencia_cantidad
                    else:
                        raise ValueError(f"No hay suficiente stock de {self.materia_prima.nombre} para actualizar la compra.")
                elif diferencia_cantidad < 0:
                    self.materia_prima.cantidad += abs(diferencia_cantidad)
                self.materia_prima.save()
        elif self.producto:
            if not self.pk:
                if self.producto.stock >= self.cantidad:
                    self.producto.stock -= self.cantidad
                    self.producto.save()
                else:
                    raise ValueError(f"No hay suficiente stock de {self.producto.nombre} para realizar el pedido.")
            else:
                original = FacturaDetalle.objects.get(pk=self.pk)
                diferencia_cantidad = self.cantidad - original.cantidad
                if diferencia_cantidad > 0:
                    if self.producto.stock >= diferencia_cantidad:
                        self.producto.stock -= diferencia_cantidad
                    else:
                        raise ValueError(f"No hay suficiente stock de {self.producto.nombre} para actualizar el pedido.")
                elif diferencia_cantidad < 0:
                    self.producto.stock += abs(diferencia_cantidad)
                self.producto.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.materia_prima:
            self.materia_prima.cantidad += self.cantidad
            self.materia_prima.save()
        elif self.producto:
            self.producto.stock += self.cantidad
            self.producto.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        tipo = 'Materia Prima' if self.materia_prima else 'Producto'
        item = self.materia_prima if self.materia_prima else self.producto
        return f"Detalle Factura - {tipo}: {item.nombre} - Cantidad: {self.cantidad}"

    class Meta:
        verbose_name = 'Detalle de Factura'
        verbose_name_plural = 'Detalles de Factura'
        db_table = 'factura_detalle'
        ordering = ['id']


class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pedidos')
    fecha_pedido = models.DateTimeField(auto_now_add=True, verbose_name='Fecha del pedido')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Subtotal', default=Decimal('0.00'), editable=False)

    def actualizar_subtotal(self):
        self.subtotal = sum(item.precio * item.cantidad for item in self.productos.all())
        self.save()

    def __str__(self):
        return f"Pedido #{self.id} - Fecha: {self.fecha_pedido} - Subtotal: {self.subtotal}"

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        db_table = 'pedido'
        ordering = ['-fecha_pedido']


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido #{self.pedido.id} - Producto: {self.producto.nombre} - Cantidad: {self.cantidad} - Precio: {self.precio}"

    class Meta:
        verbose_name = 'Producto del Pedido'
        verbose_name_plural = 'Productos del Pedido'
        db_table = 'pedido_producto'
        ordering = ['pedido', 'producto']
