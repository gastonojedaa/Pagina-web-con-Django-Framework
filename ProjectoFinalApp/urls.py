from django.urls import path
from ProjectoFinalApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.Home, name = 'home'),
    path('shop/',views.Shop, name = 'shop'),
    path('contact/',views.Contact, name = 'contact'),
    path('blog/',views.Blog, name = 'blog'),
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #poder abrir la imagen al clickear