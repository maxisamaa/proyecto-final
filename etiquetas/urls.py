from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('etiquetas/', lista_etiquetas.as_view(), name='lista_etiquetas'),
    path('etiquetas/crear/', crear_etiqueta.as_view(), name='crear_etiqueta'),
    path('etiquetas/<int:pk>/editar/', editar_etiqueta.as_view(), name='editar_etiqueta'),
    path('etiquetas/<int:pk>/eliminar/', eliminar_etiqueta.as_view(), name='eliminar_etiqueta'),
]