from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from .models import *

def products(request):
    products_inv = ProductInventory.objects.all
    return render(request, 'products.html', {'products_inv':products_inv})

def home_page(request):
    return render(request, 'home.html')

def contact_page(request):
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
			return render(request, "contact.html",{'form':form, 'successful_submit': True})
		else:
			return render(request, "contact.html", {'form':form})

	form = ContactForm()
	return render(request, "contact.html", {'form':form})