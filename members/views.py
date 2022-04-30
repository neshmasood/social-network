# from django.shortcuts import render, redirect
# from django.views import generic
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from .forms import SignUpForm
# from django.urls import reverse_lazy

# # Create your views here.


# # django auth

# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template = "Registration/signup.html"
#     success_url = reverse_lazy('login')


# def login_view(request):
#     # if POST, then authenticate the user (submitting the username and password)
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             u = form.cleaned_data['username']
#             p = form.cleaned_data['password']
#             user = authenticate(username = u, password = p)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect('/')
#                 else:
#                     return render(request, 'login.html', {'form': form})
#             else:
#                 return render(request, 'login.html', {'form': form})
#         else: 
#             return render(request, 'signup.html', {'form': form})
#     else: 
#         form = AuthenticationForm()
#         return render(request, 'login.html', {'form': form})




# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect('/')


# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/login/')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})