from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def example_api_view(request):
    data = {"message": "Hola desde Django!"}
    return Response(data)

