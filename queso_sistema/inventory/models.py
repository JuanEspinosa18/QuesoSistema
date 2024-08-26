from django.db import models

class materia_prima(models.Model):
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
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion de producto')
    valor = models.IntegerField(verbose_name='Valor')
    fecha_vencimiento = models.DateField(verbose_name='Fecha de vencimiento')
    cantidad_existente = models.IntegerField(verbose_name='Cantidad existente')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre} -> {self.valor}'
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        db_table = 'producto'
        ordering = ['id']

class orden_produccion(models.Model):
    cantidad = models.IntegerField(verbose_name='Cantidad')
    cantidad_materia_utilizada = models.IntegerField(verbose_name='Cantidad utilizada')
    fecha_orden = models.DateField(verbose_name='Fecha de orden')
    materia_prima = models.ForeignKey(materia_prima, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Orden #{self.id} - Producto: {self.producto.nombre} - Cantidad: {self.cantidad}"

    
    class Meta:
        verbose_name = 'orden produccion'
        verbose_name_plural = 'ordenes produccion'
        db_table = 'orden_produccion'
        ordering = ['id']

        
