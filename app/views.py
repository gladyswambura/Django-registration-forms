from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# Create your views here.
def  homepage(request):
    return  render(request=request, template_name= 'home.html',)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return self.success_url
    
class LoginView(generic.LoginView):
    template_name = 'login.html'