# recepcion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_equipos, name='lista_equipos'),  
    path('registrar/', views.registrar_equipo, name='registrar_equipo'),
    path('listado/', views.listado_equipos, name='listado_equipos'),
    path('detalle/<str:nombre>/', views.detalle_equipo, name='detalle_equipo'),
    path('equipos/', views.listado_equipos, name='listado_equipos'),  # Alternativa
    path('equipos/<int:id>/', views.detalle_equipo_por_id, name='detalle_equipo'),  # Cambiado para usar nueva vista
    path('equipos/<int:id>/editar/', views.editar_equipo, name='editar_equipo'),
    path('equipos/<int:id>/eliminar/', views.eliminar_equipo, name='eliminar_equipo'),
]