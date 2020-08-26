from rest_framework import serializers

from .models import PyUser


class UserSerializer(serializers.ModelSerializer):
    """Creando Serializer para enviar datos de Usuarios
    """
    class Meta:
        model = PyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'celular', 'avatar']