# views.py (en tu aplicación)
from rest_framework import generics
from .models import OrdenDeCompraAPI
from .serializers import OrdenDeCompraAPISerializer
from django.shortcuts import render
from django.views import View
import requests
from django.http import JsonResponse


class OrdenDeCompraAPIListCreateView(generics.ListCreateAPIView):
    queryset = OrdenDeCompraAPI.objects.all()
    serializer_class = OrdenDeCompraAPISerializer




class SincronizarOrdenesDeCompraView(View):
    def get(self, request, *args, **kwargs):
        api_url = "https://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?estado=todos&ticket=CD623554-7585-4416-A5D0-ED90600149FC"

        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Verificar si hay errores en la respuesta

            data = response.json()

            # Asegúrate de que la clave 'Listado' existe en los datos antes de intentar acceder a ella
            if 'Listado' in data:
                lista_ordenes = data['Listado']

                # Itera a través de la lista de órdenes y guárdalas en la base de datos
                for orden_data in lista_ordenes:
                    codigo = orden_data.get('Codigo', '')  # Accede al campo 'Codigo'
                    nombre = orden_data.get('Nombre', '')  # Puedes usar .get() para manejar claves opcionales
                    estado = orden_data.get('CodigoEstado', '')  # Accede al campo 'CodigoEstado'

                    # Crea un nuevo objeto OrdenDeCompraAPI en la base de datos
                    orden_compra = OrdenDeCompraAPI(
                        codigo=codigo,
                        nombre=nombre,
                        estado=estado
                    )
                    orden_compra.save()  # Guarda el objeto en la base de datos

                return JsonResponse({"message": "Datos sincronizados y almacenados exitosamente."})
            else:
                return JsonResponse({"message": "La clave 'Listado' no se encuentra en los datos JSON."})
        except requests.exceptions.RequestException as e:
            return JsonResponse({"message": "Error al consultar la API externa.", "error": str(e)})

