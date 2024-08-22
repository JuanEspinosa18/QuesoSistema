from django.shortcuts import render
from sales.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

    #INDEX VIEWS
def index(request):
    return render(request, 'index.html', {
    })
    
def nosotros(request):
    return render(request, 'information_nosotros/nosotros.html', {
    })
    
def nuestros_quesos(request):
    return render(request, 'information_nosotros/nuestros_quesos.html', {
    })

def nuestras_materias_prima(request):
    return render(request, 'information_nosotros/materias_prima.html', {
    })
    
    #BLOG VIEWS
def blog_informativo(request):
    return render(request, 'information_nosotros/blog_informativo.html', {
    })
    
def blog1(request):
    return render(request, 'information_nosotros/blog1.html', {
    })
    
def blog2(request):
    return render(request, 'information_nosotros/blog2.html', {
    })

def blog3(request):
    return render(request, 'information_nosotros/blog3.html', {
    })

def blog4(request):
    return render(request, 'information_nosotros/blog4.html', {
    })
    
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


    