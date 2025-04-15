from django.urls import path
from .views import ProductCreateView, ProductListView

app_name = 'products'

urlpatterns = [
    path('agregar/', ProductCreateView.as_view(), name='create'),
    path('lista/', ProductListView.as_view(), name='list'),
]