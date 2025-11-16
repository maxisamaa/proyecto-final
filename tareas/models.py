from django.db import models
from categorias.models import *
from etiquetas.models import Etiqueta
from django.contrib.auth.models import User
from django.utils.timezone import now


class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    proximidad = models.ForeignKey(Proximidad, on_delete=models.CASCADE)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # dueño de la tarea
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    fecha_termino = models.DateTimeField(null=True, blank=True)
    completada = models.BooleanField(default=False)  # Nuevo campo

    def __str__(self):
        return self.titulo
    
    def tiempo_restante(self):
        if not self.fecha_termino:
            return None
        delta = self.fecha_termino - now()
        if delta.total_seconds() <= 0:
            return None
        dias = delta.days
        horas = delta.seconds // 3600
        return {'dias': dias, 'horas': horas}