from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm, EditForm


# Create your views here.

class HomePage(TemplateView): 
    template_name = 'home.html' 


# django auth

def login_view(request):
    # if POST, then authenticate the user (submitting the username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else: 
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})




def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



class PostDetailView(DetailView): 
    model = Post
    template_name="post_detail.html"
    
    
    
class PostList(TemplateView):
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context['posts'] = Post.objects.filter(name_icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context['posts'] = Post.objects.all()
            context['header'] = "Daily Posts" # this is where we add the key into our context object for the view to use
        return context 


#CRUD on Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'author', 'image', 'body']
    template_name = "post_create.html"
    success_url = '/posts'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/posts')
    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post_update.html'
    success_url = "/posts"

    
class DeletePostView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    # success_url = reverse_lazy('/posts')
    success_url = "/posts"