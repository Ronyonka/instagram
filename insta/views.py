from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from django.contrib.auth.models import User
from .forms import NewImageForm
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.get_images()
    return render(request, 'home.html',{"images":images})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')
    else:
        form = NewImageForm()

    return render(request, 'new_image.html', {"form":form})

# @login_required(login_url='/accounts/login/')
# def profile(request,username):
#     current_user = request.user
#     try:
#         user = User.objects.get(username = username)
#         profile = Profile.objects.get(user=user)
#         images = Image.objects.filter(profile=profile)
#     except ObjectDoesNotExist:
#         return redirect('edit_profile',current_user)

#     if request.method == 'POST':
#         form = NewImageForm(request.POST,request.FILES)
#         if form.is_valid():
#             image = form.save(commit=False)
#             image.user = current_user
#             image.profile =profile
#             image.save()
#         else:
#             form = NewImageForm()
#         return render(request,"profile.html",{"profile":profile, "images":images,"form":form,})

def edit_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            bio = form.save(commit=False)
            bio.user = current_user
            bio.save()
        return redirect('index')
    elif Profile.objects.get(user=current_user):
        profile = Profile.objects.get(user=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'edit_profile.html',{"form":form})

