from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from . import models
from .forms import CustomUserCreationForm

# Create your views here.

# class SignUpView(generic. CreateView):           zamani ke az allauth estefade mikonim be class signup niaz nadarim
#     form_class = CustomUserCreationForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('home')