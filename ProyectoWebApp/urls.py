from django.urls import path

from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('', views.inicio, name='Inicio'),
    path('tienda', views.tienda, name='Tienda'), 
    path('contacto', views.contacto, name='Contacto'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)