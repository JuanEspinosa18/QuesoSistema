from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group

class UsuarioManager(BaseUserManager):
    def create_user(self, email, documento, primer_nombre, primer_apellido, password=None):
        if not documento:
            raise ValueError('El usuario debe tener un documento')
        
        usuario = self.model(
            email=self.normalize_email(email),
            documento=documento, 
            primer_nombre=primer_nombre, 
            primer_apellido=primer_apellido
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, documento, primer_nombre, primer_apellido, password=None):
        usuario = self.create_user(
            email,
            documento=documento, 
            primer_nombre=primer_nombre, 
            primer_apellido=primer_apellido,
            password=password
        )
        usuario.usuario_administrador = True
        usuario.usuario_activo = True
        usuario.save()
        return usuario
    
class Usuario(AbstractBaseUser):
    documento = models.CharField(max_length=10, unique=True, verbose_name='Documento identidad')
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico', max_length=50)
    primer_nombre = models.CharField(max_length=20, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=20, verbose_name='Segundo Nombre', blank=True, null=True)
    primer_apellido = models.CharField(max_length=20, verbose_name='Primer Apellido')
    segundo_apellido = models.CharField(max_length=20, verbose_name='Segundo Apellido', blank=True, null=True)
    telefono = models.CharField(max_length=10, verbose_name='Teléfono', blank=True, null=True)
    imagen = models.ImageField(upload_to='perfil/', max_length=50, verbose_name='Imagen de perfil', blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    
    # Relación con los grupos
    groups = models.ManyToManyField(Group, related_name='usuarios', blank=True)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['documento', 'primer_nombre', 'primer_apellido']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Se puede ajustar la lógica aquí según sea necesario
        return True

    def has_module_perms(self, app_label):
        # Se puede ajustar la lógica aquí según sea necesario
        return True

    @property
    def is_staff(self):
        return self.usuario_activo

    @property
    def is_superuser(self):
        return self.usuario_administrador

    def grupo(self):
        return ", ".join([group.name for group in self.groups.all()])
