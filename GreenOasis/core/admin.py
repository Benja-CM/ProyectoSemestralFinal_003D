from django.contrib import admin
from .models import Rol, Usuario, Categoria, Producto, Comuna, Direccion, Compra, Detalle, Historial, Pregunta, Respuesta
# Register your models here.

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Compra)
admin.site.register(Detalle)
admin.site.register(Historial)
admin.site.register(Pregunta)
admin.site.register(Respuesta)