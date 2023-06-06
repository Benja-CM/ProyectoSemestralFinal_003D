from rest_framework import serializers 
from core.models import Usuario, Direccion

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','us_rut','us_nombre','us_apellido','us_telefono','c_alias','c_correo','c_password','rol']

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['id_dir','dir_calle','dir_numero','dir_cod_postal','usuario','comuna']

