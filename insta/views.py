from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Like,Comments
from django.contrib.auth.models import User
from .forms import NewImageForm,ProfileForm,CommentForm,Registration
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.get_images()
    user = request.user
    profile = Profile.objects.all()
    return render(request, 'home.html',{"images":images,"profile":profile,"user":request.user})

@login_required(login_url='/accounts/login/')
def own_profile(request):
    user = request.user    
    images = Image.objects.all().filter(profile_id = user.id)
    return render(request, 'profile.html', {'images':images, "user":user, "current_user":request.user })

def register(request):

   if request.method == 'POST':
      form = Registration(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=raw_password)
         login(request, user)
         user = User.objects.filter
         return redirect('edit_profile')
   else:
      form = Registration()

   context = {
      'form': form
   }

   return render(request, 'edit_profile.html', context)


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
def single_image(request, image_id):
    image = Image.get_image_id(image_id)
    comments = Comments.get_comments_by_images(image_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.author = request.user
            comment.save()
            return redirect('single_image', image_id=image_id)
    else:
        form = CommentForm()

    return render(request, 'image.html', {'image':image, 'form':form, 'comments':comments})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})