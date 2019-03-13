from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Like,Comments
from django.contrib.auth.models import User
from .forms import NewImageForm,ProfileForm,CommentForm
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.get_images()
    user = request.user
    profile = Profile.objects.all()
    return render(request, 'home.html',{"images":images,"profile":profile,"user":request.user})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user= request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.profile = current_user
            picture.save()
            return redirect('home')
    else:
        form = NewImageForm()

    return render(request, 'new_image.html', {"form":form})


@login_required(login_url='/accounts/login/')
def profile(request,id):
    user = User.objects.get(id=id)
    images = Image.objects.all().filter(profile_id = user.id)
    profile = Profile.objects.all()
    return render(request, 'profile.html',{"images":images,"profile":profile,"current_user":request.user,"user":user,})


def edit_profile(request):
    current_user = request.user
  
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect("/profile/" + str(request.user.id) + "/")
    else:
        form = ProfileForm()
    return render(request, "edit_profile.html", {"form":form})  


def like(request,id):

   user = request.user

   image = Image.objects.get(id=id)
   like = image.like_set.filter(liked_by=user.profile).first()
  

   if like:
      like.delete()
   else:
      Like.likes(image,user.profile)

   return redirect('home')


@login_required(login_url='/accounts/login')
def single_image(request, id):
    image = Image.objects.get(id=id)
    comments = Comments.objects.filter(image_id = image.id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = request.user
            comment.save()
            return redirect("single_image/"+ str(image.id)+"/")
    else:
        form = CommentForm()

    return render(request, 'image.html', {'image':image, 'form':form, 'comments':comments})