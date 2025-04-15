from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order {self.id} by {self.user}"
    
    # Añadir esto (sin cambiar estructura)
    def get_total(self):
        return sum(op.product.price * op.quantity for op in self.orderproduct_set.all())

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)  # Añadido default

    def __str__(self):
        return f"{self.order} - {self.product}"