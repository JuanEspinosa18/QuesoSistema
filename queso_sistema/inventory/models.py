from django.db import models

class MateriaPrima(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción de materia prima')
    fecha_ven = models.DateField(verbose_name='Fecha de vencimiento')
    cantidad = models.IntegerField(default=0, verbose_name='Cantidad')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Materia prima'
        verbose_name_plural = 'Materias primas'
        db_table = 'materia_prima'
        ordering = ['id']


class Producto(models.Model):
    nombre = models.CharField(unique=True, max_length=200, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción de producto')
    valor = models.IntegerField(verbose_name='Valor', blank=True)
    stock = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre} -> {self.valor}'
    
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
    lote = models.ForeignKey(LoteProducto, on_delete=models.CASCADE, related_name='materias_primas')
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    cantidad_utilizada = models.IntegerField(verbose_name='Cantidad utilizada')

    def __str__(self):
        return f'{self.materia_prima.name} - Cantidad utilizada: {self.cantidad_utilizada}'
    
    class Meta:
        verbose_name = 'Materia prima del lote'
        verbose_name_plural = 'Materias primas del lote'
        db_table = 'materia_prima_lote'
        ordering = ['id']
