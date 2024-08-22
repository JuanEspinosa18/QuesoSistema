from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('nuestros_quesos/', views.nuestros_quesos, name='nuestros_quesos'),
    path('nuestras_materias_prima/', views.nuestras_materias_prima, name='nuestras_materias_prima'),
    path('blog_informativo/', views.blog_informativo, name='blog_informativo'),
    path('blog1/', views.blog1, name='blog1'),
    path('blog2/', views.blog2, name='blog2'),
    path('blog3/', views.blog3, name='blog3'),
    path('blog4/', views.blog4, name='blog4'),
    path('user/', include('users.urls')),
    path('sales/', include('sales.urls')),
    path('inventory/', include('inventory.urls')),
    path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


