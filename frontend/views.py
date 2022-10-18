from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

def products(request):
    products_inv = ProductInventory.objects.all
    return render(request, 'products.html', {'products_inv':products_inv})

def home_page(request):
    return render(request, 'home.html')