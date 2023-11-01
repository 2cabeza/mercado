#from django.contrib import admin
#from django.urls import path, include
#from orden.views import consumir_y_guardar_api
#from api_rest.views import views


#urlpatterns = [
    # Otras URL de tu aplicación
 #   path('admin/', admin.site.urls),
 #   path('consumir-y-guardar-api/', consumir_y_guardar_api, name='consumir_y_guardar_api'),
 #   path('api/', include('api_rest_mp.urls')),
 #   path('ordenes-de-compra/', views.OrdenDeCompraAPIList.as_view(), name='orden-de-compra-list'),


#]


# urls.py (en tu aplicación)
from django.urls import path
from .views import OrdenDeCompraAPIListCreateView
from .views import SincronizarOrdenesDeCompraView


urlpatterns = [
    path('ordenes-de-compra/', OrdenDeCompraAPIListCreateView.as_view(), name='orden-de-compra-list-create'),
    # Agrega más rutas de la API si es necesario.

    # urls.py (en tu aplicación)
    path('sincronizar-ordenes/', SincronizarOrdenesDeCompraView.as_view(), name='sincronizar-ordenes'),
    # Otras rutas de tu aplicación


]




