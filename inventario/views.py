# inventario/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from .models import Producto3D
from .forms import Producto3DForm


from django.contrib.auth.decorators import user_passes_test


def es_admin(user):
    return user.is_authenticated and user.is_superuser


# 1. Listar productos y Dashboard

def lista_productos(request):
    query = request.GET.get('q', '')
    
    if query:
        productos = Producto3D.objects.filter(nombre__icontains=query)
    else:
        productos = Producto3D.objects.all()

    total_productos = productos.count()
    total_stock = productos.aggregate(total=Sum('stock'))['total'] or 0
    total_filamento = productos.aggregate(total=Sum(F('filamento_g') * F('stock')))['total'] or 0
    
    valor_total = productos.aggregate(
        total=Sum(ExpressionWrapper(F('precio_venta') * F('stock'), output_field=DecimalField()))
    )['total'] or 0

    context = {
        'productos': productos,
        'query': query,
        'total_productos': total_productos,
        'total_stock': total_stock,
        'total_filamento': round(total_filamento, 1),
        'valor_total': round(valor_total, 2),
    }
    # Corregida la ruta a 'inventario/lista_productos.html'
    return render(request, 'inventario/lista_productos.html', context)

# 2. Crear producto (AQUÍ ESTÁ LA FUNCIÓN QUE FALTABA)
def crear_producto(request):
    if request.method == 'POST':
        form = Producto3DForm(request.POST, request.FILES) # <-- request.FILES
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto3DForm()
        
    return render(request, 'inventario/form_producto.html', {'form': form})
# 3. Editar producto

def editar_producto(request, id):
    producto = get_object_or_404(Producto3D, id=id)
    if request.method == 'POST':
        form = Producto3DForm(request.POST, request.FILES, instance=producto) # <-- request.FILES
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto3DForm(instance=producto)
        
    return render(request, 'inventario/form_producto.html', {'form': form, 'producto': producto})

# 4. Eliminar producto

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto3D, id=id)
    producto.delete()
    return redirect('lista_productos')

# inventario/views.py (añadir al final)

def aumentar_stock(request, id):
    producto = get_object_or_404(Producto3D, id=id)
    producto.stock += 1
    producto.save()
    return redirect('lista_productos')

def disminuir_stock(request, id):
    producto = get_object_or_404(Producto3D, id=id)
    if producto.stock > 0:
        producto.stock -= 1
        producto.save()
    return redirect('lista_productos')

# Vista pública: Todos pueden ver la lista
def lista_productos(request):
    # Lógica pública para ver productos...
    return render(request, 'lista.html')

# Vistas protegidas: Solo el admin puede modificar
@user_passes_test(es_admin, login_url='/admin/login/')
def crear_producto(request):
    # Lógica para crear un registro...
    pass

@user_passes_test(es_admin, login_url='/admin/login/')
def editar_producto(request, pk):
    # Lógica para editar un registro...
    pass

@user_passes_test(es_admin, login_url='/admin/login/')
def eliminar_producto(request, pk):
    # Lógica para eliminar un registro...
    pass
