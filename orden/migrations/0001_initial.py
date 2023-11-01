# Generated by Django 4.2.6 on 2023-10-29 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrdenDeCompra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.CharField(max_length=255)),
                ("nombre", models.CharField(max_length=255)),
                ("estado", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ItemOrdenDeCompra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("correlativo", models.CharField(max_length=255)),
                ("categoria", models.CharField(max_length=255)),
                ("codigo_producto", models.CharField(max_length=255)),
                ("producto", models.CharField(max_length=255)),
                ("especificacion_comprador", models.TextField()),
                ("cantidad", models.PositiveIntegerField()),
                ("unidad", models.CharField(max_length=255)),
                ("moneda", models.CharField(max_length=255)),
                ("precio_neto", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total_cargos", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "total_descuentos",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "total_impuestos",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "orden_compra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orden.ordendecompra",
                    ),
                ),
            ],
        ),
    ]