from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from django.contrib.auth.models import User
from .forms import NewImageForm,ProfileForm
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

@login_required (login_url='/accounts/register/')
def like_image(request):
    images = get_object_or_404(Image,id = request.POST.get('image_id') )
    is_liked = False
    if images.likes.filter(id = request.user.id).exists():
        images.likes.remove(request.user)
        is_liked = False
    else:
        images.likes.add(request.user)
        is_liked = True

    return HttpResponseRedirect(images.get_absolute_url())