from django.shortcuts import render,HttpResponse


# Create your views here.

def Home(request):
    return render(request,"ProjectoFinalApp/home.html")

def Shop(request):
    return render(request,"ProjectoFinalApp/shop.html")



