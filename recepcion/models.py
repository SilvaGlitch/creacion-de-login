# recepcion/models.py
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    cliente = models.CharField(max_length=100)
    contacto = models.CharField(max_length=50)
    descripcion_falla = models.TextField()
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='En recepción')

    def __str__(self):
        return f"{self.cliente} - {self.descripcion_falla[:50]}"
