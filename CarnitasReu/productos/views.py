from django.shortcuts import render
from .models import Producto

def home(request):
    return render(request, 'home.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

