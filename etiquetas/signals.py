from .models import Etiqueta

def crear_etiquetas_default(sender, **kwargs):
    etiquetas_default = [
        "Filosofía", "Pensamiento", "Lenguaje",
        "Cotidianidad", "Conocimiento", "Arte"
    ]
    for e in etiquetas_default:
        Etiqueta.objects.get_or_create(nombre=e)
