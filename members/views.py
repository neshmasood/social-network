# from django.shortcuts import render
from django.views import generic
from .forms import SignUpForm



# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class= SignUpForm
    template_name = 'registration/register.html'
    

