from django.urls import path
from . import views

urlpatterns = [
    path('referencia/', views.lista_referencias, name='lista_referencias'),
    path('referencia/crear/', views.crear_referencia, name='crear_referencia'),
    path('referencia/<int:id>/editar/', views.editar_referencia, name='editar_referencia'),
    path('referencia/<int:id>/eliminar/', views.eliminar_referencia, name='eliminar_referencia'),
    path('referencia/<int:id>/', views.ver_referencia, name='ver_referencia'),

    path('pensamiento/crear/', views.crear_pensamiento, name='crear_pensamiento'),
    path('pensamiento/<int:id>/editar/', views.editar_pensamiento, name='editar_pensamiento'),
    path('pensamiento/<int:id>/eliminar/', views.eliminar_pensamiento, name='eliminar_pensamiento'),
    path('pensamiento/<int:id>/', views.ver_pensamiento, name='ver_pensamiento'),
]

