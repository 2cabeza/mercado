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

# urls.py (en tu proyecto)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.urls')),
    # Otras rutas de tu proyecto
]

