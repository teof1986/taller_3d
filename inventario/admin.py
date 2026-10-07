from django.contrib import admin
from .models import Producto3D, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Producto3D)
class Producto3DAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'filamento_g', 'precio_venta', 'costo_estimado', 'ganancia_neta', 'stock')
    list_filter = ('categoria',)
    search_fields = ('nombre',)
