import pytest
from sales.models import Factura, FacturaProducto, CalificacionProducto
from users.models import CustomUser, UserProfile, Role
from inventory.models import Producto

@pytest.mark.django_db
def test_create_factura_venta():
    cliente_role = Role.objects.create(name='Cliente', description='Cliente Role')
    empleado_role = Role.objects.create(name='Empleado', description='Empleado Role')

    cliente = CustomUser.objects.create_user(
        email='cliente@gmail.com',
        password='123456',
        documento='1234567890',
        primer_nombre='Cliente',
        primer_apellido='Apellido',
        telefono='123456789'
    )
    profile = UserProfile.objects.create(user=cliente, role=cliente_role)
    cliente.profile.role = cliente_role

    
@pytest.mark.django_db
def test_create_factura_producto():
    producto = Producto.objects.create(
        nombre='Producto Test',
        descripcion='Descripción del producto',
        valor=2000,
        fecha_vencimiento='2024-12-31',
        cantidad_existente=30
    )
    
    calificacion = CalificacionProducto.objects.create(
        valor_calificacion=5,
        des_calificacion='Excelente'
    )

    factura = Factura.objects.create(
        name='Factura Test',
        fecha_factura='2024-08-16 00:00',
        subtotal=6000,
        iva=1140,
        total=7140
    )

    factura_producto = FacturaProducto.objects.create(
        cantidad=3,
        valor_productos=6000,
        calificacion_producto=calificacion,
        producto=producto,
        factura=factura
    )
    
    assert factura_producto.producto.nombre == 'Producto Test'
    assert factura_producto.cantidad == 3