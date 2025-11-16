
from django.db import models

class Tipo(models.Model):
    COLORES = [
        ('rojo', 'Tramite'),
        ('azul', 'Plan'),
        ('verde', 'academico'),
        ('amarillo', 'practica'),
    ]
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=20, choices=COLORES)
    def __str__(self):
        return self.nombre

class Proximidad(models.Model):
    OPCIONES = [
        ('corto', 'Corto Plazo'),
        ('mediano', 'Mediano Plazo'),
        ('largo', 'Largo Plazo'),
    ]
    valor = models.CharField(max_length=20, choices=OPCIONES)
    def __str__(self):
        return self.get_valor_display()

class Prioridad(models.Model):
    NIVELES = [
        ('muy alta', 'muy Alta'),
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]
    nivel = models.CharField(max_length=20, choices=NIVELES)
    orden = models.IntegerField()  # 1 = más importante
    def __str__(self):
        return f"{self.get_nivel_display()} (orden {self.orden})"


