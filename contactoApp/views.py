from django.shortcuts import render,HttpResponse
from .forms import formContacto

# Create your views here.

def Contact(request):
    formulario_contacto = formContacto()
    return render(request,"contact/contact.html",{"miFormulario": formulario_contacto})