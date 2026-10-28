from django.db import models
from django.utils import timezone


# Create your models here.
class   Dato(models.Model):
    nombre=models.CharField(unique=True,null=False)
    Valor=models.FloatField(default=0)
    Fecha=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"En el salon, tengo {self.nombre} con {self.Valor} a las {self.Fecha}"