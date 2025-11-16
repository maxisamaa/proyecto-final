from django.apps import AppConfig


class EtiquetasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'etiquetas'

    def ready(self):
        from .models import Etiqueta
        etiquetas_default = [
            "Filosofía", "Pensamiento", "Lenguaje",
            "Cotidianidad", "Conocimiento", "Arte"
        ]
        for e in etiquetas_default:
            Etiqueta.objects.get_or_create(nombre=e)
