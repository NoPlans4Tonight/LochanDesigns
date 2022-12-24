from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import GalleryUploadForm
from django.core.files import File
from .forms import GalleryUploadForm
from .forms import GalleryUploadForm
from storage.models import *
from PIL import Image
from resizeimage import resizeimage
import tempfile
import os

# Create your views here.
def products(request):
	p = Paginator(Storage.objects.exclude(product_name='Background'), 6)
	
	page = request.GET.get('page')
	products = p.get_page(page)

	return render(request, 'products.html', {'page_obj': products})

def edit_products(request):
	return render(request, 'maintenance/maintenance.html')

def upload_product(request):
	if request.method == 'POST':
		form = GalleryUploadForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return HttpResponse('successfully uploaded')
	else:
		form = GalleryUploadForm()

	form = GalleryUploadForm()
	return render(request, 'maintenance/upload.html', {"form": form})