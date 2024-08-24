from django.shortcuts import render

# Create your views here.
def nosotros(request):
    return render(request, 'nosotros.html', {
    })
    
def nuestros_quesos(request):
    return render(request, 'nuestros_quesos.html', {
    })

def nuestras_materias_prima(request):
    return render(request, 'materias_prima.html', {
    })
    
    #BLOG VIEWS
def blog_informativo(request):
    return render(request, 'blog_informativo.html', {
    })
    
def blog1(request):
    return render(request, 'blog1.html', {
    })
    
def blog2(request):
    return render(request, 'blog2.html', {
    })

def blog3(request):
    return render(request, 'blog3.html', {
    })

def blog4(request):
    return render(request, 'blog4.html', {
    })