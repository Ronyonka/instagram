from django import forms
from .models import Image,Profile

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image_path', 'caption')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']