from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.template.defaultfilters import slugify

class Profile(models.Model):
    profile_picture = models.ImageField(blank=True, upload_to='profiles/')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def save_user(self):
        self.save

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls,id):
        profile = Profile.objects.get(user=id)
        return profile
    
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def get_absolute_url(self):
        return reverse('user_profile')

    @classmethod
    def search_by_username(cls,user):
        person = User.objects.filter(username__icontains = user)[0]
        return cls.objects.filter(profile__id = person.id)
        

class Image(models.Model):
    image_path =  models.ImageField(upload_to="images/")
    # name= models.CharField(max_length=30)
    caption = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    likes = models.ManyToManyField(User, blank=True,related_name='post_likes')
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.filter(id=self.id).delete()

    def update_caption(self,val):
        Image.objects.filter(id=self.id).update(caption=val)

    @classmethod
    def get_images(cls):
        return cls.objects.all()

    @classmethod
    def show_image(cls,profile):
        images =  cls.objects.filter(profile__user=profile)
        return images

