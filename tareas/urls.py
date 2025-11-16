from django.urls import path
from .views import *
from .views import index

urlpatterns = [
    path('', index, name='index'), 
    path('tareas/', ListaTareas.as_view(), name='lista_tareas'),
    path('tareas/crear/', CrearTarea.as_view(), name='crear_tarea'),
    path('tareas/editar/<int:pk>/', EditarTarea.as_view(), name='editar_tarea'),
    path('tareas/eliminar/<int:pk>/', EliminarTarea.as_view(), name='eliminar_tarea'),
    path('tareas/<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
    path('vida_en_semanas/', vida_en_semanas, name='vida_en_semanas'),

]