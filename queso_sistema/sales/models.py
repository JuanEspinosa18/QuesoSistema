from django.conf import settings
from django.db import models
from decimal import Decimal

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), editable=False)

    def calcular_subtotal(self):
        # Calcula el subtotal solo si el pedido ya tiene una clave primaria
        if self.pk:
            return sum(item.precio * item.cantidad for item in self.productos.all())
        return Decimal('0.00')

    def save(self, *args, **kwargs):
        # Calcula el subtotal al guardar el pedido
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
        if not self.pk:  # Nueva instancia
            if self.producto.stock >= self.cantidad:
                self.producto.stock -= self.cantidad
                self.producto.save()
            else:
                raise ValueError(f"No hay suficiente stock de {self.producto.nombre} para realizar el pedido.")
        else:  # Actualización
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

# Modelo de Factura (relaciona un pedido con una factura)
from decimal import Decimal

class Factura(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='factura')
    fecha_factura = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de factura')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Subtotal', default=Decimal('0.00'))
    iva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='IVA', default=Decimal('0.00'))
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total', default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        # Calcular el subtotal sumando el precio * cantidad de cada producto en el pedido
        self.subtotal = self.pedido.subtotal
        iva_rate = Decimal('0.12')  # IVA del 12%
        self.iva = self.subtotal * iva_rate
        self.total = self.subtotal + self.iva
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Factura #{self.id} - Pedido #{self.pedido.id} - Total: {self.total}"

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        db_table = 'factura'
        ordering = ['id']

class FacturaVenta(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='ventas_factura')
    empleado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ventas_empleado')
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ventas_cliente')

    def __str__(self):
        return f"Factura Venta - Empleado: {self.empleado.email} - Cliente: {self.cliente.email}"

    class Meta:
        verbose_name = 'Factura venta'
        verbose_name_plural = 'Facturas de ventas'
        db_table = 'factura_venta'
        ordering = ['id']

class FacturaCompra(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='compras_factura')
    proveedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='compras_proveedor')
    empleado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='compras_empleado')

    def __str__(self):
        return f"Factura Compra - Proveedor: {self.proveedor.email} - Empleado: {self.empleado.email}"

    class Meta:
        verbose_name = 'Factura de compra'
        verbose_name_plural = 'Facturas de compras'
        db_table = 'factura_compra'
        ordering = ['id']
