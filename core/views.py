from django.shortcuts import render
from .models import Item
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')

def HomePage(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home-page.html', context)

def CheckoutPage(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'checkout-page.html', context)

def ProductPage(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'product-page.html', context)