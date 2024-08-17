from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    documento = models.IntegerField(verbose_name='Número de Documento')
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

class Role(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del Rol', unique=True)
    description = models.TextField(verbose_name='Descripción del Rol')

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Rol')

    def __str__(self):
        return f"Perfil de {self.user.email}"
