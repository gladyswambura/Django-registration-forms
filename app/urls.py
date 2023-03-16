from  django.urls  import  path
from . import views 
from .views import *

urlpatterns = [
path('', views.homepage, name='homepage'),
path("signup/", views.SignUpView, name="signup"),
path('login/', LoginView.as_view(), name='login'),
path('accounts/profile/', views.profile, name='profile'),
path('accounts/profile/', views.profile_edit, name='profile_edit'),
]