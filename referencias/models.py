
from django.db import models
from django.contrib.auth.models import User
from etiquetas.models import Etiqueta

class Referencias(models.Model): # tiene una relacion de uno es a muchos con usuarios , siempre el muchos es el que recibe la clave foranea
    nombre=models.CharField(max_length=200)
    autor=models.CharField(max_length=200)
    autor=models.CharField(max_length=200,blank=True)
    descripcion=models.TextField()
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    def __str__(self):
        return self.nombre 
    
class Pensamientos(models.Model):
    nombre = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # ahora es usuario logueado
    descripcion = models.TextField()
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)

    def __str__(self):
        return self.nombre

    

    

