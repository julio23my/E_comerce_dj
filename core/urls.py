from django.urls import path

from .views import *

app_name='core'

urlpatterns = [
    path('', index, name='index'),
    path('home/',HomeView.as_view() , name='home'),
    path('checkout/',CheckoutPage , name='checkout'),
    path('product/<slug>/',ItemDetailView.as_view() , name='product'),
    path('add-to-cart/<slug>/',add_to_cart , name='add-to-cart'),
]