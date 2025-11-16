
from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.categorias_panel, name='categorias_menu'),
]