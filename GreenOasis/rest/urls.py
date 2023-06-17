"""Rest URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from .views import lista_usuario, detalle_usuario, lista_direccion, detalle_direccion
from rest.viewslogin import login

urlpatterns = [
    path('lista_usuario/', lista_usuario, name='lista_usuario'),
    path('detalle_usuario/<id>', detalle_usuario, name='detalle_usuario'),
    path('lista_direccion/', lista_direccion, name='lista_direccion'),
    path('detalle_direccion/<id>', detalle_direccion, name='detalle_direccion'),
    path('lista_direccion/', lista_direccion, name='lista_direccion'),
    path('detalle_direccion/<id>', detalle_direccion, name='detalle_direccion'),
    path('login', login, name="login"),
]