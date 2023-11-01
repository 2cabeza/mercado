from django.conf import settings
from django.db import models
from django.utils import timezone


class OrdenDeCompraAPI(models.Model):
    codigo = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    created_date = models.DateTimeField(
            default=timezone.now)

    # Agrega otros campos según sea necesario

    def __str__(self):
        return self.codigo
