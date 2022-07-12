from django.shortcuts import render,HttpResponse

# Create your views here.

def Home(request):
    return render(request,"ProjectoFinalApp/home.html")

def Services(request):
    return render(request,"ProjectoFinalApp/services.html")

def Shop(request):
    return render(request,"ProjectoFinalApp/shop.html")

def Blog(request):
    return render(request,"ProjectoFinalApp/blog.html")

def Contact(request):
    return render(request,"ProjectoFinalApp/contact.html")