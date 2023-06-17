from rest_framework import serializers 
from core.models import Usuario, Direccion, Detalle

from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','us_rut','us_nombre','us_apellido','us_telefono','c_alias','c_correo','c_password','rol']
        
    def create(self, validated_data):
        # Crear el usuario en el modelo Usuario
        usuario = Usuario.objects.create(**validated_data)

        # Crear el usuario en el modelo User
        user = User.objects.create(username=usuario.c_alias, email=usuario.c_correo)
        user.set_password(usuario.c_password)
        user.save()

        return usuario
    
class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = ['id_detalle','compra','producto','de_cantidad','de_subtotal']

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['id_dir','dir_calle','dir_numero','dir_cod_postal','usuario','comuna']
