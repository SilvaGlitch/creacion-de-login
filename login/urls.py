from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),      # ruta principal: login
    path('logout/', views.logout_view, name='logout'),  # ruta para cerrar sesión
]
