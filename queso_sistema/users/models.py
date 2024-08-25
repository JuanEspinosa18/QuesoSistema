from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
import re

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo de correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
    
def validar_documento_identidad(value):
    # Verifica que solo contenga números
    if not re.match(r'^\d+$', value):
        raise ValidationError('El documento de identidad solo puede contener números.')
    # Verifica la longitud
    if len(value) < 8 or len(value) > 10:
        raise ValidationError('El documento de identidad debe tener entre 8 y 10 caracteres.')

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    documento = models.CharField(max_length=10, validators=[validar_documento_identidad],unique=True, verbose_name='documento identidad')
    primer_nombre = models.CharField(max_length=200, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=200, verbose_name='Segundo Nombre', blank=True, null=True)
    primer_apellido = models.CharField(max_length=200, verbose_name='Primer Apellido')
    segundo_apellido = models.CharField(max_length=200, verbose_name='Segundo Apellido', blank=True, null=True)
    telefono = models.CharField(max_length=10, verbose_name='Teléfono', blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['documento', 'primer_nombre', 'primer_apellido']

    def __str__(self):
        return self.email
    
    def grupo(self):
        return ", ".join([group.name for group in self.groups.all()])