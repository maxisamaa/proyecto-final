from django.db import models

# Create your models here.
from django.db import models  # Asegúrate de ajustar el import según tu estructura real

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
