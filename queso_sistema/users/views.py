from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser, UserProfile, Role
from django.db import IntegrityError
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        documento = request.POST['documento']
        primer_nombre = request.POST['primer_nombre']
        segundo_nombre = request.POST['segundo_nombre']
        primer_apellido = request.POST['primer_apellido']
        segundo_apellido = request.POST['segundo_apellido']
        telefono = request.POST['telefono']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden')
        else:
            # Verificar si el correo electrónico ya está en uso
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ingresado ya está registrado. Por favor, elija otro.')
            else:
                try:
                    # Crear el usuario personalizado
                    user = CustomUser.objects.create_user(email=email, 
                                                        documento=documento,
                                                        primer_nombre=primer_nombre,
                                                        segundo_nombre=segundo_nombre,
                                                        primer_apellido=primer_apellido,
                                                        segundo_apellido=segundo_apellido,
                                                        telefono=telefono,
                                                        password=password)
                    
                    # Asignar el rol de cliente al perfil del usuario
                    cliente_role = Role.objects.get(name='Cliente')  # Asegúrate de tener el rol correcto en tu base de datos
                    UserProfile.objects.create(user=user, role=cliente_role)

                    # Iniciar sesión después de registrar con éxito
                    login(request, user)

                    messages.success(request, '¡Usuario creado con éxito!')
                    return redirect('login')  # Redirigir a la página de inicio de sesión después de registrar con éxito
                except IntegrityError:
                    messages.error(request, 'Hubo un error al crear el usuario. Por favor, inténtalo de nuevo.')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('admin:index')  # Redirige al panel de administrador si es superusuario
            elif user.profile.role.name == 'Cliente':
                return redirect('carrito')  # Redirige al carrito si es cliente
            else:
                return redirect('DashVentas')  # Redirige al dashboard de ventas si es empleado
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, '¡Sesión finalizada con éxito!')
    return redirect('login')

    #FOMULARIO CONTACTO
def contacto(request):
    mensaje_enviado = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            
            # Enviar correo
            send_mail(
                f'Mensaje de {nombre} con el correo: {email}',
                mensaje,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            mensaje_enviado = True
    else:
        form = ContactForm()
    
    return render(request, 'contacto.html', {'form': form, 'mensaje_enviado': mensaje_enviado})

