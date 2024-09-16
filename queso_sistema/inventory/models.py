from django.db import models
from users.models import Proveedor

class MateriaPrima(models.Model):
    nombre = models.CharField(unique=True, max_length=200, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción de materia prima')
    stock = models.IntegerField(default=0, verbose_name='Stock')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Materia prima'
        verbose_name_plural = 'Materias primas'
        db_table = 'materia_prima'
        ordering = ['id']

class Producto(models.Model):
    nombre = models.CharField(unique=True, max_length=200, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción de producto')
    precio = models.IntegerField(verbose_name='Precio', blank=True)
    stock = models.IntegerField(default=0, verbose_name='Stock')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    descontinuado = models.BooleanField(default=False, verbose_name='Descontinuado')

    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']

class LoteProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto = models.IntegerField(verbose_name='Cantidad producida')
    fecha_produccion = models.DateField(verbose_name='Fecha de producción')
    fecha_vencimiento = models.DateField(verbose_name='Fecha de vencimiento')

    def __str__(self):
        return f'Lote de {self.producto.nombre} - Cantidad producida: {self.cantidad_producto}'

    class Meta:
        verbose_name = 'Lote de producción'
        verbose_name_plural = 'Lotes de producción'
        db_table = 'lote_produccion'
        ordering = ['id']

class MateriaPrimaLote(models.Model):
    lote_producto = models.ForeignKey(LoteProducto, on_delete=models.CASCADE, related_name='materias_primas')
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    cantidad_utilizada = models.IntegerField(verbose_name='Cantidad utilizada')

    def __str__(self):
        return f'{self.materia_prima.nombre} - Cantidad utilizada: {self.cantidad_utilizada}'
    
    class Meta:
        verbose_name = 'Materia prima del lote'
        verbose_name_plural = 'Materias primas del lote'
        db_table = 'materia_prima_lote'
        ordering = ['id']

class EntradaMateriaPrima(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='entradas')
    fecha_entrada = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de entrada')
    fecha_vencimiento = models.DateField(verbose_name='Fecha de vencimiento', null=True, blank=True)
    total_costo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total costo', default=0.00)

    def __str__(self):
        return f"Entrada #{self.id} - Proveedor: {self.proveedor.nombre} - Total Costo: {self.total_costo}"

    class Meta:
        verbose_name = 'Entrada de Materia Prima'
        verbose_name_plural = 'Entradas de Materia Prima'
        db_table = 'entrada_materia_prima'
        ordering = ['-fecha_entrada']
