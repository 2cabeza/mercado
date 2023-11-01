from django.contrib import admin
from .models import OrdenDeCompraAPI

#admin.site.register(OrdenDeCompra)
#admin.site.register(ItemOrdenDeCompra)


class OrdenDeCompraAPIAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'created_date', 'estado')



# Register the admin class with the associated model
admin.site.register(OrdenDeCompraAPI, OrdenDeCompraAPIAdmin)

