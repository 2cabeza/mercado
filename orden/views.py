import requests
from django.http import HttpResponse
from .models import OrdenDeCompra, ItemOrdenDeCompra

def consumir_y_guardar_api(request):
    #api_url = "https://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?fecha=26102023&CodigoProveedor=1545807&ticket=CD623554-7585-4416-A5D0-ED90600149FC"
    api_url = "https://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?codigo=1195104-295-AG23&ticket=CD623554-7585-4416-A5D0-ED90600149FC"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            for orden_data in data.get('Listado', []):
                # Utiliza update_or_create para buscar o crear una orden según el campo 'codigo'
                orden, created = OrdenDeCompra.objects.update_or_create(
                    codigo=orden_data.get('Codigo'),
                    defaults={
                        'nombre': orden_data.get('Nombre'),
                        'estado': orden_data.get('Estado', 'Sin estado'),
                        # Agrega más campos según sea necesario
                    }
                )

                # Procesar e insertar los ítems de la orden
                items_data = orden_data.get('Items', {}).get('Listado', [])
                for item_data in items_data:
                    # Utiliza update_or_create para buscar o crear un ítem según el campo 'Correlativo'
                    item, created = ItemOrdenDeCompra.objects.update_or_create(
                        orden_compra=orden,
                        correlativo=item_data.get('Correlativo'),
                        defaults={
                            'categoria': item_data.get('Categoria'),
                            'codigo_producto': item_data.get('CodigoProducto'),
                            'producto': item_data.get('Producto'),
                            'especificacion_comprador': item_data.get('EspecificacionComprador'),
                            'cantidad': item_data.get('Cantidad'),
                            'unidad': item_data.get('Unidad'),
                            'moneda': item_data.get('Moneda'),
                            'precio_neto': item_data.get('PrecioNeto'),
                            'total_descuentos': item_data.get('TotalDescuentos'),
                            'total_impuestos': item_data.get('TotalImpuestos'),
                            'total': item_data.get('Total'),
                            # Agrega otros campos según sea necesario
                        }
                    )

            return HttpResponse('Datos de la API almacenados en la base de datos.')

        else:
            return HttpResponse('Error al obtener datos de la API')

    except Exception as e:
        return HttpResponse('Error: ' + str(e))
