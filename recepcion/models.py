# recepcion/models.py
from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    cliente = models.CharField(max_length=100)
    contacto = models.CharField(max_length=50)
    descripcion_falla = models.TextField()
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='En recepción')

    def __str__(self):
        return f"{self.cliente} - {self.descripcion_falla[:20]}"
