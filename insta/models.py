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

    def __str__(self):
        return f'{self.user}'

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
    profile = models.ForeignKey(Profile)
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

class Comments(models.Model):
    text = models.CharField(max_length = 100, blank = True)
    image = models.ForeignKey(Image, related_name = "comments")
    author = models.ForeignKey(User, related_name = "author")
    created_date = models.DateTimeField(auto_now_add = True,null = True)
    approved_comment = models.BooleanField(default=False)


 
    def save_comment(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

    def delete_comment(self):
        Comments.objects.get(id = self.id).delete()
    
    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments
        
    def __str__(self):
        return self.text

