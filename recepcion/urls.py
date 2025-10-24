# recepcion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_equipos, name='lista_equipos'),  
    path('registrar/', views.registrar_equipo, name='registrar_equipo'),
    path('listado/', views.listado_equipos, name='listado_equipos'),
    path('detalle/<str:nombre>/', views.detalle_equipo, name='detalle_equipo'),
]
