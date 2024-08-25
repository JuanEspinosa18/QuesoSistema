from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'documento', 'primer_nombre', 'primer_apellido', 'telefono', 'is_staff', 'is_active', 'grupo')

