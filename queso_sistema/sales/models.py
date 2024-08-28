from django.conf import settings
from django.db import models
from decimal import Decimal
from django.core.exceptions import ValidationError
from inventory.models import MateriaPrima  

# Modelo Pedido (relacionado a ventas)
class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), editable=False)

    def calcular_subtotal(self):
        if self.pk:
            return sum(item.precio * item.cantidad for item in self.productos.all())
        return Decimal('0.00')

    def save(self, *args, **kwargs):
        self.subtotal = self.calcular_subtotal()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido #{self.id} - Usuario: {self.usuario.email} - Subtotal: {self.subtotal}"

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        db_table = 'pedido'
        ordering = ['id']

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='productos')
    producto = models.ForeignKey('inventory.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.producto.stock >= self.cantidad:
                self.producto.stock -= self.cantidad
                self.producto.save()
            else:
                raise ValueError(f"No hay suficiente stock de {self.producto.nombre} para realizar el pedido.")
        else:
            original = PedidoProducto.objects.get(pk=self.pk)
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
        self.producto.stock += self.cantidad
        self.producto.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Pedido #{self.pedido.id} - Producto: {self.producto.nombre} - Cantidad: {self.cantidad}"

    class Meta:
        verbose_name = 'Pedido Producto'
        verbose_name_plural = 'Pedidos Productos'
        db_table = 'pedido_producto'
        ordering = ['id']

# Modelo Factura (base para ventas y compras)

#modelo facturas general
class Factura(models.Model):
    TIPO_FACTURA_CHOICES = [
        ('venta', 'Venta'),
        ('compra', 'Compra'),
    ]
    tipo_factura = models.CharField(max_length=10, choices=TIPO_FACTURA_CHOICES, default='venta')
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

# Modelo FacturaVenta (factura de ventas)
class FacturaVenta(Factura):
    pedido = models.OneToOneField('Pedido', on_delete=models.CASCADE, related_name='factura', null=True, blank=True)
    empleado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ventas_empleado')
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ventas_cliente')

    def save(self, *args, **kwargs):
        # Calcula el subtotal sumando los precios de los productos en el pedido
        self.subtotal = sum(item.precio * item.cantidad for item in self.pedido.productos.all())
        # Calcula el IVA (por ejemplo, 19%)
        self.iva = self.subtotal * Decimal('0.19')
        # Calcula el total
        self.total = self.subtotal + self.iva
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Factura Venta - Empleado: {self.empleado.email} - Cliente: {self.cliente.email}"

    class Meta:
        verbose_name = 'Factura venta'
        verbose_name_plural = 'Facturas de ventas'
        db_table = 'factura_venta'
        ordering = ['id']


# Modelo FacturaCompra (factura de compras)
class FacturaCompra(Factura):
    proveedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='compras_proveedor')
    empleado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='compras_empleado')
    factura_compra_detalles = models.ManyToManyField('FacturaCompraDetalle', related_name='facturas', blank=True)

    def save(self, *args, **kwargs):
        # Guarda la instancia primero para asegurarse de que tenga un ID
        if not self.pk:
            super().save(*args, **kwargs)
        
        # Calcula el subtotal sumando los precios de los detalles de compra
        self.subtotal = sum(item.precio * item.cantidad for item in self.factura_compra_detalles.all())
        # Calcula el IVA (por ejemplo, 19%)
        self.iva = self.subtotal * Decimal('0.19')
        # Calcula el total
        self.total = self.subtotal + self.iva
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Factura Compra - Proveedor: {self.proveedor.email} - Empleado: {self.empleado.email}"

    class Meta:
        verbose_name = 'Factura de compra'
        verbose_name_plural = 'Facturas de compras'
        db_table = 'factura_compra'
        ordering = ['id']

# Modelo FacturaCompraDetalle (detalles de las compras de materia prima)
class FacturaCompraDetalle(models.Model):
    factura_compra = models.ForeignKey('FacturaCompra', on_delete=models.CASCADE, related_name='detalles_compra', null=True, blank=True)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio por unidad')

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.materia_prima.cantidad >= self.cantidad:
                self.materia_prima.cantidad -= self.cantidad
                self.materia_prima.save()
            else:
                raise ValueError(f"No hay suficiente stock de {self.materia_prima.nombre} para realizar la compra.")
        else:
            original = FacturaCompraDetalle.objects.get(pk=self.pk)
            diferencia_cantidad = self.cantidad - original.cantidad
            if diferencia_cantidad > 0:
                if self.materia_prima.cantidad >= diferencia_cantidad:
                    self.materia_prima.cantidad -= diferencia_cantidad
                else:
                    raise ValueError(f"No hay suficiente stock de {self.materia_prima.nombre} para actualizar la compra.")
            elif diferencia_cantidad < 0:
                self.materia_prima.cantidad += abs(diferencia_cantidad)
            self.materia_prima.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.materia_prima.cantidad += self.cantidad
        self.materia_prima.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        factura_id = self.factura_compra.id if self.factura_compra else 'No asignada'
        return f"Factura Compra #{factura_id} - Materia Prima: {self.materia_prima.nombre} - Cantidad: {self.cantidad}"

    class Meta:
        verbose_name = 'Detalle de Factura de Compra'
        verbose_name_plural = 'Detalles de Facturas de Compra'
        db_table = 'factura_compra_detalle'
        ordering = ['id']
