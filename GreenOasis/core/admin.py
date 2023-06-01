from django.contrib import admin
from .models import Rol, Usuario, Categoria, Producto, Region, Comuna, Direccion, Estado, Compra, Detalle 
# Register your models here.

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Estado)
admin.site.register(Compra)
admin.site.register(Detalle)
