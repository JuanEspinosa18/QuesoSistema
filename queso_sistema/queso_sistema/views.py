from django.shortcuts import render
from django.http import HttpResponseServerError

    #INDEX VIEWS
def index(request):
    return render(request, 'index.html', {
    })
    
#Vista de los errores
def error_404_view(request, exception=None):
    return render(request, 'Error404.html', status=404)


def error_500_view(request, exception=None):
    return render(request, 'Error500.html', status=500)

#Vista de prueba del error 500
def test_error_500(request):
    raise Exception("This is a test error.")