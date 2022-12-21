from django.shortcuts import render
from django.core.paginator import Paginator
from storage.models import *

# Create your views here.
def products(request):
	p = Paginator(Storage.objects.exclude(product_name='Background'), 6)
	page = request.GET.get('page')
	products = p.get_page(page)

	return render(request, 'products.html', {'page_obj': products})
