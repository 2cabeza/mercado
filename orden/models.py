from django.conf import settings
from django.db import models
from django.utils import timezone


class OrdenDeCompra(models.Model):
    codigo = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    created_date = models.DateTimeField(
            default=timezone.now)

    # Agrega otros campos según sea necesario

    def __str__(self):
        return self.codigo


class ItemOrdenDeCompra(models.Model):
    orden_compra = models.ForeignKey(OrdenDeCompra, on_delete=models.CASCADE)
    correlativo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    codigo_producto = models.CharField(max_length=255)
    producto = models.CharField(max_length=255, null=True, blank=True)
    especificacion_comprador = models.TextField()
    cantidad = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    unidad = models.CharField(null=True, blank=True, max_length=255)
    moneda = models.CharField(null=True, blank=True, max_length=255)
    precio_neto = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    total_cargo = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    total_descuentos = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    total_impuestos = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    total = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    # Agrega otros campos según sea necesario

    def __str__(self):
        return self.correlativo
