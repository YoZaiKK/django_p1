from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect, render

# Create your views here.


def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)

    return redirect("Tienda")


def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)

    return redirect("Tienda")


def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto)

    return redirect("Tienda")


def limpiar_carro(request):
    carro = Carro(request)
    carro.vaciar()

    return redirect("Tienda")