from django.shortcuts import render
# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView

from .forms import UserCreationForm, LoginForm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class LogIn(LoginView):
    form_class = LoginForm
    # success_url = reverse_lazy('index')
    template_name = 'login.html'