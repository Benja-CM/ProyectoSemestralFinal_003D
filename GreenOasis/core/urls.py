"""Core URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from .views import index, product, profile

urlpatterns = [
    path('', index, name='index'),
    path('product1/', product, name='producto'),
    path('profile/', profile, name='perfil'),
]