# Generated by Django 4.2.6 on 2023-10-29 03:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("orden", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordendecompra",
            name="created_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
