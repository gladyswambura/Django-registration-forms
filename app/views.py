from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

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

