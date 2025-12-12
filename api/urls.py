from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from .views import api_info

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'equipos', EquipoViewSet)
router.register(r'diagnosticos', DiagnosticoViewSet)
router.register(r'entregas', EntregaViewSet)

urlpatterns = [
    path('', api_info, name='api-info'),
    path('token/login/', obtain_auth_token, name='api-login'),
    path('', include(router.urls)),
]