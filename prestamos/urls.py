from django.urls import path
from .cliente_view import cliente_create, cliente_all, cliente_get, cliente_update, cliente_delete
from .prenda_view import prenda_all, prenda_get, prenda_create, prenda_update, prenda_delete, prenda_get_fk
from .detalle_cliente_view import detalle_cliente_create, detalle_cliente_get, detalle_cliente_all

urlpatterns = [
    # rutas de Clientes
    path('clientes/', cliente_all, name = 'clientes'),
    path('clientes/<int:pk>', cliente_get, name = 'cliente'),
    path('clientes/create', cliente_create, name = 'cliente-create'),
    path('clientes/update/<int:pk>', cliente_update, name = 'clientes-update'),
    path('clientes/delete/<int:pk>', cliente_delete, name = 'clientes-delete'),
    # rutas de Prenda
    path('prendas/', prenda_all, name = 'prendas'),
    path('prendas/<int:pk>', prenda_get, name='prenda'),
    path('prendas/fk/<int:fk>', prenda_get_fk, name='prenda-fk'),
    path('prendas/create', prenda_create, name = 'prendas-create'),
    path('prendas/update/<int:pk>', prenda_update, name='prendas-update'),
    path('prendas/delete/<int:pk>', prenda_delete, name = 'prendas-delete'),
    #rutas de detalle_cliente
    path('detalle-cliente/', detalle_cliente_all, name = 'detalle-cliente'),
    path('detalle-cliente/<int:fk>', detalle_cliente_get, name='detalle-cliente'),
    path('detalle-cliente/create', detalle_cliente_create, name = 'detalle-cliente-create'),


]

