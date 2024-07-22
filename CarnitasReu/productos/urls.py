from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('productos/', views.lista_productos, name='lista_productos'),  # Página de lista de productos
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),  # Detalle de producto
]








