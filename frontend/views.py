from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ContactForm
from .models import *
from storage.models import Storage

def products(request):
	p = Paginator(ProductInventory.objects.all(), 6)
	page = request.GET.get('page')
	products = p.get_page(page)

	return render(request, 'products.html', {'page_obj': products})

def home_page(request):
	storageRecord = Storage.objects.filter(product_name='Background')
	bg = storageRecord
	return render(request, 'main.html', {'bg':bg})

def contact_page(request):
	storageRecord = Storage.objects.filter(product_name='Background')
	bg = storageRecord
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			"First Name: " + form.cleaned_data['first_name'], 
			"Last Name: " + form.cleaned_data['last_name'], 
			"Email: " + form.cleaned_data['email_address'], 
			"Message: " + form.cleaned_data['message'], 
			}
			message = "\n".join(body)
			try:
				send_mail(subject, message, 'haley@lochandesigns.com', ['haley@lochandesigns.com', 'jlochan53@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render(request, "contact.html",{'form':form, 'successful_submit': True, 'bg': bg})
		else:
			return render(request, "contact.html", {'form':form, 'bg': bg})

	form = ContactForm()
	return render(request, "contact.html", {'form':form, 'bg': bg})