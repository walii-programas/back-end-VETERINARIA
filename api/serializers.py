from rest_framework import serializers
from veterinaria.models import Veterinario, Servicios, Blog


class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = ['id', 'CMVP', 'Nombre_Apellidos', 'Telefono_Celular', 'Direccion', 'Foto']


class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ['id', 'Nombre', 'Descripcion', 'Foto']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'Nombre', 'Descripcion', 'Foto']
