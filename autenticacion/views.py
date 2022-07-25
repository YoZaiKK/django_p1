from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

# def autenticacion(request):
#     return render(request, "registro/registro.html")

class VRegistro(View):
    def get(self, request): # Esta funcion es la encargada de mostrarnos nuestro form
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form": form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            usuario = form.save()
            login(request, usuario)
            return redirect("Inicio") 
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {"form": form})
        
def cerrar_sesion(request):
    logout(request)
    return redirect("Inicio")

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usr = form.cleaned_data.get("username")
            contra_usr = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usr, password=contra_usr)
            if usuario is not None:
                login(request, usuario)
                return redirect("Inicio")
            else: 
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or wrong info")
    form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})
    