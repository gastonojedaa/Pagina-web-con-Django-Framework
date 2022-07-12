from django.urls import path
from ProjectoFinalApp import views

urlpatterns = [
    
    path('',views.Home, name = 'home'),
    path('services/',views.Services, name = 'services'),
    path('shop/',views.Shop, name = 'shop'),
    path('contact/',views.Contact, name = 'contact'),
    path('blog/',views.Blog, name = 'blog'),
    
]