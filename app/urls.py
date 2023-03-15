from  django.urls  import  path
from . import views 
from .views import *

urlpatterns = [
path('', views.homepage, name='homepage'),
path("signup/", SignUpView.as_view(), name="signup"),
path('login/', LoginView.as_view(), name='login'),
]