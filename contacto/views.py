from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage 

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido') 
            emailEnviado = EmailMessage("Mensaje desde el app de contacto", 
                                 "El usuario {} con la dirreccion {} escribe lo siguiente:\n\n{}".format(nombre, email, contenido),
                                 "",
                                 ["memocuentaparadjango@gmail.com"],
                                 reply_to = [email])
            try: 
                emailEnviado.send()
                return redirect("/contacto/?valido")
            except Exception as e:
                print(e)
                return redirect("/contacto/?novalido")
    return render(request, 'contacto/contacto.html', {"miFormulario": formulario_contacto})