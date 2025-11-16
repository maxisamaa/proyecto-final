from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    # --- Referencias ---
    path('referencias/', views.lista_referencias, name='lista_referencias'),
    path('referencias/nuevo/', views.crear_referencia, name='crear_referencia'),
    path('referencias/editar/<int:id>/', views.editar_referencia, name='editar_referencia'),
    path('referencias/eliminar/<int:id>/', views.eliminar_referencia, name='eliminar_referencia'),

    # --- Pensamientos ---
    path('pensamientos/nuevo/', views.crear_pensamiento, name='crear_pensamiento'),
    path('pensamientos/editar/<int:id>/', views.editar_pensamiento, name='editar_pensamiento'),
    path('pensamientos/eliminar/<int:id>/', views.eliminar_pensamiento, name='eliminar_pensamiento'),
]
