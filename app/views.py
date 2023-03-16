from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def  homepage(request):
    return  render(request=request, template_name= 'home.html',)

def SignUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('form')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
    
class LoginView(LoginView):
    template_name = 'login.html'


def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile_edit')
    else:
        form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'registration/profile_edit.html', {'form': form})

def form(request):
    return render(request, 'form.html')