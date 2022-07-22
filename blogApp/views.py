from django.shortcuts import render
from blogApp.models import post, category

# Create your views here.

def Blog(request):
    posts = post.objects.all()  #listar todos los posts
    return render(request,"blog/blog.html",{"posts":posts})

def categoriaFilter(request,category_id):
    categoria = category.objects.get(id=category_id)  #obtener todas las categorias
    posts = post.objects.filter(categories = categoria) #filtrar posts por categorias
    return render(request,"blog/categorias.html",{'categoria':categoria,"posts":posts})
