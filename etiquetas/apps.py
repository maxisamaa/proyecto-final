from django.apps import AppConfig
from django.db.models.signals import post_migrate

class EtiquetasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'etiquetas'

    def ready(self):
        from .signals import crear_etiquetas_default
        post_migrate.connect(crear_etiquetas_default, sender=self)
