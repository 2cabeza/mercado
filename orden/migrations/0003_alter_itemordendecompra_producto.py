# Generated by Django 4.2.6 on 2023-10-29 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orden", "0002_ordendecompra_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemordendecompra",
            name="producto",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
