from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):  # Cambiado de Form a ModelForm
#porque asi evito repetir campos de manera manual
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available', 'photo']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'available': 'Disponible',
            'photo': 'Foto',
        }
#Y el metodo save se elimina porque al usar ModelForm ya se implementa