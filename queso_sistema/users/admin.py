from django.contrib import admin
from .models import CustomUser, Role, UserProfile
from django.contrib.admin import AdminSite
from django.shortcuts import redirect

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'documento', 'primer_nombre', 'primer_apellido', 'telefono', 'is_staff', 'is_active')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
