from rest_framework import serializers
from .models import Cliente, Detalle_cliente, Prenda

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class Detalle_clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_cliente
        fields = '__all__'

class PrendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prenda
        fields = '__all__'