from django.urls import path

from . import views 

app_name = 'carro'

urlpatterns = [  
    path('agregar/<producto_id>/', views.agregar_producto, name = "agregar"),  
    path('restar/<producto_id>/', views.restar_producto, name = "restar"),  
    path('eliminar/<producto_id>/', views.eliminar_producto, name = "eliminar"),  
    path('limpiar/', views.limpiar_carro, name = "limpiar"),  
] 
 