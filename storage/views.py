from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.files import File
from .forms import GalleryUploadForm, EditRecordForm
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
    storage_records = Storage.objects.all()
    return render(request, 'maintenance/maintenance.html', {'storage_records': storage_records})

def edit_record(request, record_id):
    record = Storage.objects.get(id=record_id)
    if request.method == 'POST':
        # Process the updated form data and save it
        form = EditRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            # return redirect(f'/products/edit-record/{record_id}/')
            return redirect(reverse('storage:edit'))
    else:
        # Render the form with the current record data
        form = EditRecordForm(instance=record)
    
    return render(request, 'maintenance/edit_record.html', {'form': form, 'record': record})

def delete_record(request, record_id):
    record = Storage.objects.get(id=record_id)
    record.delete()
    return redirect(reverse('storage:edit'))

def upload_product(request):
    if request.method == 'POST':
        form = GalleryUploadForm(request.POST, request.FILES)
        if request.FILES:
            if form.is_valid():
                product = form.save(commit=False)  # Save the form data temporarily
                
                # Resize the image if necessary
                image = form.cleaned_data['image']
                if image.size > 1000000:
                    resized_image, size = resize_image(image)
                    
                    # Check if the resized image size is within the limit
                    if size <= 1000000:
                        # Save the resized image to product.image field
                        product.image.save(image.name, File(resized_image))
                    else:
                        # Image cannot be resized to the required size
                        messages.error(request, 'The image size is too large')
                        return redirect('/products')  # or handle the error appropriately
                
                product.save()  # Save the product model with the resized image
                return redirect('/products')
    else:
        messages.error(request, 'Something went wrong')
    
    form = GalleryUploadForm()
    return render(request, 'maintenance/upload.html', {"form": form})

def resize_image(image):
    # Open the image
    img = Image.open(image)
    
    # Resize the image
    resized_img = resizeimage.resize_cover(img, [800, 800])
    
    # Create a temporary file to save the resized image
    temp_image = tempfile.NamedTemporaryFile(delete=True)
    resized_img.save(temp_image.name, img.format)
    
    # Get the size of the resized image
    size = os.path.getsize(temp_image.name)
    
    return temp_image, size