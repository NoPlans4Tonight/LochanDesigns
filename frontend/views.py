from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm, CreateUserForm
from .models import *
from storage.models import Storage

def products(request):
	p = Paginator(ProductInventory.objects.all(), 6)
	page = request.GET.get('page')
	products = p.get_page(page)

	return render(request, 'products.html', {'page_obj': products})

def home_page(request):
	# storageRecord = Storage.objects.filter(product_name='Background')
	storageRecord = Storage.objects.order_by('?')[:1]
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

def register_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')

		context = {'form':form}
		return render(request, "register.html", context)

def login_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, "login.html", context)

def logout_user(request):
	logout(request)
	return redirect('login')