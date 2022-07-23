from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# def autenticacion(request):
#     return render(request, "registro/registro.html")

class VRegistro(View):
    def get(self, request): # Esta funcion es la encargada de mostrarnos nuestro form
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form": form})
    
    def post(self, request):
        pass
