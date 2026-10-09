from django.contrib import admin
from .models import Producto3D


@admin.register(Producto3D)
class Producto3DAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'stock', 'precio_venta', 'filamento_g')
    search_fields = ('nombre',)
