"""Core URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from .views import index, product, profile, cart, search, conf_pago, create_acc, h_buy, h_prod1, p_acc, p_info
from .views import p_pch, pss_fg, vent_edit, vent_ing, vent_list, ong, registrarInfUS, registrarInfAC, registrarTarjeta, resgistrarProducto

urlpatterns = [
    path('', index, name='index'),
    path('product1/', product, name='producto'),
    path('profile/', profile, name='profile'),
    path('ong/', ong, name='ong'),
    path('cart/', cart, name='cart'),
    path('search/', search, name='search'),
    path('conf_pago/', conf_pago, name='conf_pago'),
    path('create_acc/', create_acc, name='create_acc'),
    path('h_buy/', h_buy, name='h_buy'),
    path('h_prod1/', h_prod1, name='h_prod'),
    path('p_acc/', p_acc, name='p_acc'),
    path('p_info/', p_info, name='p_info'),
    path('p_pch/', p_pch, name='p_pch'),
    path('pss_fg/', pss_fg, name='pss_fg'),
    path('vent_edit/', vent_edit, name='vent_edit'),
    path('vent_ing/', vent_ing, name='vent_ing'),
    path('vent_list/', vent_list, name='vent_list'),
    path('registrarInfUS/', registrarInfUS, name="registrarInfUS"),
    path('registrarInfAC/', registrarInfAC, name="registrarInfAC"),
    path('registrarTarjeta/', registrarTarjeta, name='registrarTarjeta'),
    path('resgistrarProducto/', resgistrarProducto, name='resgistrarProducto'),
]
