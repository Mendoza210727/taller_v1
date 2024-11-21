from django.http import JsonResponse

def data_view(request):
    data = {"message": "Hola desde Django!"}
    return JsonResponse(data)
