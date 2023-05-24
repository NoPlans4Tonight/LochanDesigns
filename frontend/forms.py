from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms import ClearableFileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
	botcatcher = forms.CharField(required=False,
								widget=forms.HiddenInput,
								validators=[validators.MaxLengthValidator(0)])
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'label label-default text-light'
		self.helper.field_class = 'form-control'
		self.helper.layout = Layout(
			'first_name',
			'last_name',
			'email_address',
			'message',
			'botcatcher',
			Submit('submit', 'Submit', css_class='btn btn-secondary')
		)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
