from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Blog, name = 'blog'),
    path('categoria/<int:category_id>/',views.categoriaFilter, name = 'categoria'), #para filtrar por categorias
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #poder abrir la imagen al clickear