from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Detalle_cliente
from . serializers import Detalle_clienteSerializer

@api_view(['POST'])
def detalle_cliente_create(request):
    serializer = Detalle_clienteSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'error':'No se pudo crear el detalle'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detalle_cliente_all(request):
    detalle = Detalle_cliente.objects.all()
    serializer = Detalle_clienteSerializer(detalle, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def detalle_cliente_get(request, fk):
    try:
        detalle = Detalle_cliente.objects.filter(fk_cliente = fk)
    except Detalle_cliente.DoesNotExist:
        return Response({'error':'Detalles no encontrados'}, status = status.HTTP_400_BAD_REQUEST)
    serializer = Detalle_clienteSerializer(detalle, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)