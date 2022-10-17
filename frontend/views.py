from django.shortcuts import render
from .models import *

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

def home_page(request):
    return render(request, 'home.html')