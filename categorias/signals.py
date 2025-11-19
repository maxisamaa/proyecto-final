# categorias/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Tipo, Proximidad, Prioridad

@receiver(post_migrate)
def crear_datos_default(sender, **kwargs):
    # Asegurarnos de que solo se ejecute para esta app
    if sender.name != "categorias":
        return

    # Tipos
    tipos_default = [
        ("Trámite", "rojo"),
        ("Plan", "azul"),
        ("Academico", "verde"),
        ("practica", "amarillo"),
    ]
    for nombre, color in tipos_default:
        Tipo.objects.get_or_create(nombre=nombre, color=color)

    # Proximidades
    proximidades_default = ["corto", "mediano", "largo"]
    for valor in proximidades_default:
        Proximidad.objects.get_or_create(valor=valor)

    # Prioridades
    prioridades_default = [
        ("muy alta", 1),
        ("alta", 2),
        ("media", 3),
        ("baja", 4),
    ]
    for nivel, orden in prioridades_default:
        Prioridad.objects.get_or_create(nivel=nivel, orden=orden)
