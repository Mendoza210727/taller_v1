from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=80, blank = False)
    apellidos = models.CharField(max_length=200, blank = False)
    fecha_nacimiento = models.DateField(blank=False)
    telefono = models.CharField( max_length=8, blank=False)
    genero = models.CharField(max_length=1, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Detalle_cliente(models.Model):
    detalle = models.TextField(blank = False)
    ocupacion = models.CharField(max_length=150, blank= False)
    fecha_inicio_ocupacion =  models.DateField(blank=False)
    total_ingresos = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    tipo_ocupacion = models.CharField(max_length=150, blank=False)
    fk_cliente = models.ForeignKey(Cliente, on_delete = models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Prenda(models.Model):
    descripcion = models.TextField(blank=False)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2, blank=False),
    estado = models.CharField(max_length=50, blank=False)
    fecha_resepcion = models.DateTimeField( auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null= True)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null= True)

