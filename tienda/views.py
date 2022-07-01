from django.shortcuts import render, HttpResponse

# Create your views here.

def tienda(request):

    return render(request, 'tienda/tienda.html')