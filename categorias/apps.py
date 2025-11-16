# categorias/apps.py
from django.apps import AppConfig

class CategoriasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categorias'

    def ready(self):
        from .models import Tipo, Proximidad, Prioridad

        # Precrear Tipos
        tipos_default = [
            ("Trámite", "rojo"),
            ("Plan", "azul"),
            ("Academico", "verde"),
            ("practica", "amarillo"),
        ]
        for nombre, color in tipos_default:
            Tipo.objects.get_or_create(nombre=nombre, color=color)

        # Precrear Proximidad
        proximidades_default = [
            "corto",  # Corto Plazo
            "mediano",  # Mediano Plazo
            "largo",  # Largo Plazo
        ]
        for valor in proximidades_default:
            Proximidad.objects.get_or_create(valor=valor)

        # Precrear Prioridad
        prioridades_default = [
            ("muy alta", 1),
            ("alta", 2),
            ("media", 3),
            ("baja", 4),
        ]
        for nivel, orden in prioridades_default:
            Prioridad.objects.get_or_create(nivel=nivel, orden=orden)
