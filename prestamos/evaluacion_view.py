
from .models import Prenda, Cliente, Detalle_cliente
from . serializers import PrendaSerializer, ClienteSerializer, Detalle_clienteSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

