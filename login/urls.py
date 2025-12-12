from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),     
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.logout_view, name='logout'),  
    path('api-demo/', views.demo_api, name='demo-api'),  
]
