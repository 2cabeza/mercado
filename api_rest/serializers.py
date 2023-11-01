# serializers.py (en tu aplicación)
from rest_framework import serializers
from .models import OrdenDeCompraAPI

class OrdenDeCompraAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDeCompraAPI
        fields = '__all__'
