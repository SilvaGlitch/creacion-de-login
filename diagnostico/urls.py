# diagnostico/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('asignar/', views.asignar_equipo, name='asignar_equipo'),
    path('evaluar/', views.evaluar_equipo, name='evaluar_equipo'),
    path('listado/', views.listado_diagnosticos, name='listado_diagnosticos'),
]
