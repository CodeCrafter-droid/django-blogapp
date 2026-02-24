from django.urls import path, include
from .forms import CustomLoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',LoginView.as_view(template_name='registration/login.html',authentication_form=CustomLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/',views.register,name='register'),
]