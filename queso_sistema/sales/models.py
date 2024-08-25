from django.conf import settings
from django.db import models
from inventory.models import Producto

class Factura(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre', unique=True)
    fecha_factura = models.DateTimeField(verbose_name='Fecha de factura')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Subtotal')
    iva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='IVA')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total')

    def __str__(self):
        return self.name

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

class CalificacionProducto(models.Model):
    valor_calificacion = models.IntegerField(verbose_name='Valor')
    des_calificacion = models.TextField(verbose_name='Descripción')

    def __str__(self):
        return str(self.valor_calificacion)

    class Meta:
        verbose_name = 'Calificación Producto'
        verbose_name_plural = 'Calificaciones de Productos'
        db_table = 'calificacion_producto'
        ordering = ['id']

class FacturaProducto(models.Model):
    cantidad = models.IntegerField(verbose_name='Cantidad')
    valor_productos = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor de los productos')
    calificacion_producto = models.ForeignKey(CalificacionProducto, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)

    def __str__(self):
        return f"Factura Producto - Cantidad: {self.cantidad} - Producto: {self.producto.nombre}"

    class Meta:
        verbose_name = 'Factura Producto'
        verbose_name_plural = 'Facturas de Productos'
        db_table = 'factura_producto'
        ordering = ['id']
