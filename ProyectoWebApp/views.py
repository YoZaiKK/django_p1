from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):

    return render(request, 'ProyectoWebApp/inicio.html')



def tienda(request):

    return render(request, 'ProyectoWebApp/tienda.html')


def blog(request):

    return render(request, 'ProyectoWebApp/blog.html')


def contacto(request):

    return render(request, 'ProyectoWebApp/contacto.html')
