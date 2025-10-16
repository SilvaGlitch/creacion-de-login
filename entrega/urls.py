# entrega/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('verificar/', views.verificar_cliente, name='verificar_cliente'),
    path('reporte/', views.reporte_entrega, name='reporte_entrega'),
    path('comprobante/', views.comprobante_entrega, name='comprobante_entrega'),
]
