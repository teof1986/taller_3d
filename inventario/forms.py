# inventario/forms.py
from django import forms
from .models import Producto3D

class Producto3DForm(forms.ModelForm):
    class Meta:
        model = Producto3D
        fields = '__all__'  # Toma automáticamente TODOS los campos de Producto3D
        labels = {
            'nombre': 'Nombre del Modelo 3D',
            'precio_venta': 'Precio de Venta ($)',
            'stock': 'Unidades en Stock',
            'filamento_g': 'Gramos de Filamento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'filamento_g': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }