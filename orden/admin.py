from django.contrib import admin
from .models import OrdenDeCompra, ItemOrdenDeCompra

#admin.site.register(OrdenDeCompra)
#admin.site.register(ItemOrdenDeCompra)


class OrdenDeCompraAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'created_date', 'estado')



class ItemOrdenDeCompraAdmin(admin.ModelAdmin):
    list_display = ('orden_compra', 'correlativo', 'precio_neto')


# Register the admin class with the associated model
admin.site.register(OrdenDeCompra, OrdenDeCompraAdmin)
admin.site.register(ItemOrdenDeCompra, ItemOrdenDeCompraAdmin)
