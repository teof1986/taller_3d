from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto3D(models.Model):
    nombre = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    filamento_g = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, help_text="Gramos de filamento")
    costo_material = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    costo_tiempo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    stock = models.IntegerField(default=0)

    @property
    def costo_estimado(self):
        # Suma del costo de material y costo de tiempo de impresión
        return self.costo_material + self.costo_tiempo

    @property
    def precio_min(self):
        return self.costo_estimado

    @property
    def ganancia_neta(self):
        return self.precio_venta - self.costo_estimado

    def __str__(self):
        return self.nombre
