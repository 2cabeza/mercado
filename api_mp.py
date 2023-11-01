import requests

# URL de la API
url = "https://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json"

# Parámetros de la solicitud
params = {
    "fecha": "26102024",
    "CodigoProveedor": "1545807",
    "ticket": "CD623554-7585-4416-A5D0-ED90600149FC"
}

try:
    # Realizar la solicitud GET
    response = requests.get(url, params=params)

    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # Convertir la respuesta JSON en un diccionario de Python
        data = response.json()

        # Aquí puedes procesar y trabajar con los datos en 'data'
        print(data)
    else:
        print(f"Error al hacer la solicitud a la API. Código de estado: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")
