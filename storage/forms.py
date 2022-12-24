from django import forms
from django.forms import ModelForm
from storage.models import Storage

class GalleryUploadForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['product_name', 'description', 'image']
