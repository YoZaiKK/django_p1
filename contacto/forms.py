from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label = "Nombre", max_length=100, required = True, widget=forms.TextInput(attrs={'placeholder': 'My name...'}))
    email = forms.CharField(label = "Email", max_length=100, required = True, widget=forms.TextInput(attrs={'placeholder': 'user@example.com'}))
    contenido = forms.CharField(label = "Contenido", widget=forms.Textarea(attrs={'placeholder': 'Comenario...'}))
    