from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import send_mail 
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido

# Create your views here.

@login_required(login_url="/autenticacion/iniciar_sesion")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user = request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id = str(key),
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido,
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    enviar_mail(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombre_usr = request.user.username,
        email_usuario = request.user.email
    )
    messages.success(request, "El pedido se ha creado correctamenet")
    
    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto = "Gracias por su compra"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_usr": kwargs.get("nombre_usr"),
        })
    mensaje_texto = strip_tags(mensaje) 
    from_email = 'memocuentaparadjango@gmail.com'
    to = kwargs.get("email_usuario") 
    send_mail(
        asunto,
        mensaje_texto,
        from_email,
        [to],
        html_message= mensaje,            
    )
    
    
    
    
    