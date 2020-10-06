from django.urls import path

from .views import *

app_name='core'

urlpatterns = [
    path('', index, name='index'),
    path('home/',HomePage , name='home'),
    path('checkout/',CheckoutPage , name='checkout'),
    path('itemi/',ProductPage , name='item-u'),
]