from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.template.defaultfilters import slugify

class Profile(models.Model):
    profile_picture = models.ImageField(null=True, upload_to='profiles/')
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
    
    @classmethod
    def get_profile_by_username(cls, user):
        profiles = cls.objects.filter(user__contains=user)
        return profiles

    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def get_absolute_url(self):
        return reverse('user_profile')

    # @classmethod
    # def search_by_username(cls,user):
    #     person = User.objects.filter(username__icontains = user)[0]
    #     return cls.objects.filter(profile__id = person.id)
        
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

class Image(models.Model):
    image_path =  models.ImageField(upload_to="images/")
    caption = HTMLField(null=True)
    profile = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
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
    def get_image_id(cls, id):
        image = Image.objects.get(pk=id)
        return image

    @classmethod
    def filter_by_user(cls,profile):
        the_user = User.objects.get(username = profile)
        return cls.objects.filter(profile__id = the_user.id)

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


    def __str__(self):
        return self.comment

 
    def save_comment(self):
       self.save()

       

    def delete_comment(self):
        Comments.objects.get(id = self.id).delete()
    
    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments
        
    def __str__(self):
        return self.text

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments

class Like(models.Model):

   liked = models.ForeignKey(Image, on_delete=models.CASCADE)
   liked_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

   @classmethod
   def likes(cls,img,prfl):
      like = cls(liked=img,liked_by=prfl)
      return like.save()

   def delete_like(self):
      like = Like.objects.all(self)
      return like.delete()

