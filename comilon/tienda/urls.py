from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('salir/', views.salir, name='salir'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
    path('pedido/', views.pedido, name='pedido'),
    path('agregar/', views.agregar, name='agregar'),
]
