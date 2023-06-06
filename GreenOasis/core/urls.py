"""Core URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from .views import index, product1, profile, cart, search, conf_pago, create_acc, h_buy, h_prod1, p_acc, p_info, p_pch, pss_fg, vent_edit
from .views import vent_ing, vent_list, ong, registrarInfUS, registrarInfAC, registrarProducto, eliminarProducto, eliminarDetalle
from .views import actualizarProducto, actualizarCuenta, iniciar_sesion, cerrar_sesion, registrarProducto, userInfo, userAcc, registrarDetalle

urlpatterns = [
    path('', index, name='index'),
    path('product1/<int:id>/', product1, name='product1'),
    path('profile/', profile, name='profile'),
    path('ong/', ong, name='ong'),
    path('cart/', cart, name='cart'),
    path('search/<int:categoria_id>/', search, name='search'),
    path('conf_pago/', conf_pago, name='conf_pago'),
    path('create_acc/', create_acc, name='create_acc'),
    path('h_buy/', h_buy, name='h_buy'),
    path('h_prod1/', h_prod1, name='h_prod'),
    path('p_acc/', p_acc, name='p_acc'),
    path('p_info/', p_info, name='p_info'),
    path('p_pch/', p_pch, name='p_pch'),
    path('pss_fg/', pss_fg, name='pss_fg'),
    path('vent_edit/<int:id>/', vent_edit, name='vent_edit'),
    path('vent_ing/', vent_ing, name='vent_ing'),
    path('vent_list/', vent_list, name='vent_list'),
    path('registrarInfUS/', registrarInfUS, name="registrarInfUS"),
    path('registrarInfAC/', registrarInfAC, name="registrarInfAC"),
    path('registrarProducto/', registrarProducto, name='registrarProducto'),
    path('eliminarProducto/<int:id>/', eliminarProducto, name='eliminarProducto'),
    path('actualizarProducto/', actualizarProducto, name='actualizarProducto'),
    path('actualizarCuenta/', actualizarCuenta, name='actualizarCuenta'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('registrarProducto/<int:id_prod>/<int:precio>/', registrarProducto, name='registrarProducto'),
    path('registrarDetalle/<int:id_detalle>/<int:precio>/', registrarDetalle, name='registrarDetalle'),
    path('userInfo/', userInfo, name='userInfo'),
    path('userAcc/', userAcc, name='userAcc'),
    path('eliminarDetalle/<int:id>/', eliminarDetalle, name='eliminarDetalle'),
]
