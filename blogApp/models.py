from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length= 50)    
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class post(models.Model):
    title = models.CharField(max_length= 50)
    content = models.CharField(max_length= 50)
    image= models.ImageField(upload_to = 'blog',null = True, blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #si el autor borra le usuario se borra todo (se relaciona al autor con el post)
    categories = models.ManyToManyField(category)#Una categoria puede estar en varios posts y un post puede estar en varias categorias

    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title