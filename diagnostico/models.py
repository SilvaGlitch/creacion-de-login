# diagnostico/models.py
from django.db import models
from recepcion.models import Equipo

class Diagnostico(models.Model):
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)
    tecnico = models.CharField(max_length=100)
    descripcion = models.TextField()
    solucion_propuesta = models.TextField()
    fecha_diagnostico = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnóstico {self.equipo.id}"

