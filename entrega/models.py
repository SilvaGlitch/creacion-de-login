# entrega/models.py
from django.db import models
from recepcion.models import Equipo

class Entrega(models.Model):
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    recibido_por = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Entrega {self.equipo.id}"

