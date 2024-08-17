import pytest
from inventory.models import Producto, materia_prima

@pytest.mark.django_db
def test_create_producto():
    producto = Producto.objects.create(
        nombre='Producto Test',
        descripcion='Descripción del producto',
        valor=1000,
        fecha_vencimiento='2024-12-31',
        cantidad_existente=50
    )
    assert producto.nombre == 'Producto Test'
    assert producto.cantidad_existente == 50

@pytest.mark.django_db
def test_create_materia_prima():
    materia = materia_prima.objects.create(
        name='Materia Test',
        descripcion='Descripción de la materia prima',
        fecha_ven='2024-12-31',
        cantidad=100
    )
    assert materia.name == 'Materia Test'
    assert materia.cantidad == 100