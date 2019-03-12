from django import forms
from .models import Image,Profile,Comments

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image_path', 'caption')

class  CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']