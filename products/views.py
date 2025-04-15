from django.urls import reverse_lazy
from django.views import generic
from .models import Product
from .forms import ProductForm

class ProductCreateView(generic.CreateView):
    """Vista para crear nuevos productos"""
    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'  # Ubicación correcta de la plantilla
    success_url = reverse_lazy('products:list')  # Nombre de URL (no confundir con la ruta)

class ProductListView(generic.ListView):
    """Vista para listar todos los productos"""
    model = Product
    template_name = 'products/list_product.html'  # Ubicación correcta
    context_object_name = 'products'  # Perfecto para usar en la plantilla