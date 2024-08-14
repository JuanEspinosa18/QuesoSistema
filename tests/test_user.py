import pytest
from users.models import CustomUser 

@pytest.mark.django_db
def test_user_creation():
    user = CustomUser.objects.create_user(
        email = 'gaes6@gmail.com',
        password = '123456',
        documento = 564861382,
        primer_nombre = 'Carlos',
        primer_apellido = 'Buitrago'
    )
    assert user.email == 'gaes6@gmail.com'