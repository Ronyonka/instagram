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
def profile(request):
    user = request.user
    images = Image.objects.all()
    profile = Profile.objects.all()
    return render(request, 'profile.html',{"images":images,"current_user":request.user,"user":user,})
