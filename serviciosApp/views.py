from django.shortcuts import render
from serviciosApp.models import service

# Create your views here.
def Services(request):

    services = service.objects.all() #importa todos los servicios que tengo guardados
    return render(request,"services/services.html",{"services":services})