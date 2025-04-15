from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Order, OrderProduct
from .forms import OrderProductForm  # Asumo que tienes este form básico

class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"

    def get_object(self):
        return Order.objects.filter(user=self.request.user, is_active=True).first()

class CreateOrderProductView(LoginRequiredMixin, CreateView):
    form_class = OrderProductForm
    success_url = reverse_lazy('my_order')

    def form_valid(self, form):
        order = Order.objects.filter(user=self.request.user, is_active=True).first()
        if not order:
            order = Order.objects.create(user=self.request.user)
        form.instance.order = order
        return super().form_valid(form)