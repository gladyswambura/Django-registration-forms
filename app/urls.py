from  django.urls  import  path
from . import views 
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
path('', views.homepage, name='homepage'),
path("signup/", views.SignUpView, name="signup"),
path('login/', LoginView.as_view(), name='login'),
path('form/', views.form, name='form'),
path('accounts/profile/', views.profile, name='profile'),
path('accounts/edit_profile/', views.profile_edit, name='profile_edit'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]