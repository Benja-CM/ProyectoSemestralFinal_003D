"""Rest URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from .views import lista_usuario, detalle_usuario
from rest.viewslogin import login

urlpatterns = [
    path('lista_usuario/', lista_usuario, name='lista_usuario'),
    path('detalle_usuario/<id>', detalle_usuario, name='detalle_usuario'),
    path('login', login, name="login")
]