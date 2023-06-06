"""Rest URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from .views import lista_usuario

urlpatterns = [
    path('lista_usuario/', lista_usuario, name='lista_usuario'),
]