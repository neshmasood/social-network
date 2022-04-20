from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

# Create your views here.

class HomePage(TemplateView): 
    template_name = 'home.html' 



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})