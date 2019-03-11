from django import forms
from .models import Image

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile','name','likes','pub_date']