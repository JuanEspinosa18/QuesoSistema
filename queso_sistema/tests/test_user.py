import pytest
from users.models import CustomUser, UserProfile, Role

@pytest.mark.django_db
def test_user_creation():
    user = CustomUser.objects.create_user(
        email='gaes6@gmail.com',
        password='123456',
        documento=564861382,
        primer_nombre='Carlos',
        primer_apellido='Buitrago'
    )
    assert user.check_password('123456')
    
@pytest.mark.django_db
def test_assign_role_to_user():
    user = CustomUser.objects.create_user(
        email='testuser@gmail.com',
        password='123456',
        documento=123456789,
        primer_nombre='Test',
        primer_apellido='User'
    )
    role = Role.objects.create(name='Cliente', description='Cliente Role')
    profile = UserProfile.objects.create(user=user, role=role)
    
    assert profile.role.name == 'Cliente' 