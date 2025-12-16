from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Etiqueta, DetalleProducto
from .forms import ProductoForm, DetalleForm, CategoriaForm, EtiquetaForm
from django.db.models import Q

# 1. Página de Inicio
def index(request):
    return render(request, 'index.html')

# 2. Lista de Productos (Con Consultas ORM y Raw)
def lista_productos(request):
    query = request.GET.get('q')
    # ORM: Filter
    if query:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(categoria__nombre__icontains=query)
        )
    else:
        productos = Producto.objects.all()
    
    # Ejemplo SQL Raw (Punto 6 de la evaluación)
    # productos_raw = Producto.objects.raw('SELECT * FROM core_producto')
    
    return render(request, 'productos/lista.html', {'productos': productos})

# 3. Crear Producto (Maneja Producto y Detalle a la vez)
def crear_producto(request):
    if request.method == 'POST':
        form_prod = ProductoForm(request.POST)
        form_det = DetalleForm(request.POST)
        if form_prod.is_valid() and form_det.is_valid():
            producto = form_prod.save()
            detalle = form_det.save(commit=False)
            detalle.producto = producto
            detalle.save()
            return redirect('lista_productos')
    else:
        form_prod = ProductoForm()
        form_det = DetalleForm()
    
    return render(request, 'productos/crear.html', {'form_prod': form_prod, 'form_det': form_det, 'accion': 'Crear'})

# 4. Ver Producto
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    # Seguridad: get_object_or_404 maneja error 404 si no existe
    return render(request, 'productos/detalle.html', {'producto': producto})

# 5. Editar Producto
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    try:
        detalle = producto.detalleproducto
    except DetalleProducto.DoesNotExist:
        detalle = None

    if request.method == 'POST':
        form_prod = ProductoForm(request.POST, instance=producto)
        form_det = DetalleForm(request.POST, instance=detalle)
        if form_prod.is_valid() and form_det.is_valid():
            form_prod.save()
            det = form_det.save(commit=False)
            det.producto = producto
            det.save()
            return redirect('lista_productos')
    else:
        form_prod = ProductoForm(instance=producto)
        form_det = DetalleForm(instance=detalle)

    return render(request, 'productos/crear.html', {'form_prod': form_prod, 'form_det': form_det, 'accion': 'Editar'})

# 6. Eliminar Producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar.html', {'object': producto, 'tipo': 'producto'})

# Vistas simples para Categorías y Etiquetas (Reutilizando lógica similar)
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/formulario.html', {'form': form})

def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'etiquetas/lista.html', {'etiquetas': etiquetas})

def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas') 
        form = EtiquetaForm()
    return render(request, 'categorias/formulario.html', {'form': form, 'titulo': 'Crear Etiqueta'})

# 2. Eliminar Etiqueta
def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')
    return render(request, 'productos/eliminar.html', {'object': etiqueta, 'tipo': 'etiqueta'})