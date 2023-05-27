from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from storage.models import Storage

class GalleryUploadForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ['product_name', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.add_input(Submit('submit', 'Save'))

class EditRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = Storage
        fields = ['product_name', 'description']