from django.urls import path
from ProjectoFinalApp import views

urlpatterns = [
    
    path('',views.Home, name = 'Home'),
    path('services/',views.Services, name = 'Services'),
    path('shop/',views.Shop, name = 'Shop'),
    path('blog/',views.Blog, name = 'Blog'),
    path('contact/',views.Contact, name = 'Contact')
]