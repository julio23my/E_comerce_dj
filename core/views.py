from django.shortcuts import render, get_list_or_404, redirect
from .models import Item, Order, OrderItem
from django.views.generic import ListView, DetailView
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')


class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'


def CheckoutPage(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'checkout-page.html', context)

def ProductPage(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'product.html', context)

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'


def add_to_cart(request, slug):
    item = get_list_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(item=item,
                                          user=request.user,
                                          ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect('core:product',slug=slug)