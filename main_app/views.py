from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from django.urls import reverse_lazy, reverse
from .forms import PostForm, EditForm, CommentForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.contrib.auth import get_user_model
# from django.views import generic 


# Create your views here.

class HomePage(TemplateView): 
    template_name = 'home.html' 
    
class Dashboard(TemplateView): 
    template_name = 'dashboard.html' 


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
    
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        # this will look up id of the post we would be on at that time.
        post_likes = get_object_or_404(Post, id=self.kwargs['pk']) 
        total_likes = post_likes.total_likes()
        liked = False
        if post_likes.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"] = liked
        context["total_likes"] = total_likes
        return context
        
    
    
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
    # form_class = PostForm
    fields = ['title', 'author', 'body']
    #take out image from post form
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
    


class AddCommentView(CreateView):
    model = Comment
    fields = ['author', 'body']
    # fields = '__all__'
    # form_class = CommentForm
    template_name = "comment_add.html"
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = '/posts'

# class AddCommentView(CreateView):
#     model = Comment
#     fields = ['author', 'body']
#     # fields = '__all__'
#     # form_class = CommentForm
#     template_name = "comment_add.html"
    
    
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect('/posts')
    
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     form.instance.post_id = self.kwargs['pk']
    #     # form.instance.user = self.request.user
    #     self.object.user = self.request.user
    #     self.object.save()
        
    #     return super().form_valid(form)
    # success_url = '/posts'
    
      
    
# class AddCommentView(CreateView):
#     model = Comment
#     # fields = ['name', 'body']
#     # fields = '__all__'
#     form_class = CommentForm
#     template_name = "comment_add.html"
    
    
#     # def form_valid(self, form):
#     #     self.object = form.save(commit=False)
#     #     self.object.user = self.request.user
#     #     self.object.save()
#     #     return HttpResponseRedirect('/posts')
    
#     def form_valid(self, form):
#         form.instance.post_id = self.kwargs['pk']
#         # form.instance.user = self.request.user
#         self.object.user = self.request.user
#         self.object.save()
        
#         return super().form_valid(form)
#     success_url = '/posts'
    
    
    
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.post_id = self.kwargs['pk']
    #     self.object.save()
    #     return HttpResponseRedirect('/posts')
    
    

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))





@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author__username=username)
    return render(request, 'profile.html', {'user': user, 'posts': posts})


# @login_required

# def ProfileView(request, username):
#     user = User.objects.get(username = username)
#     posts = Post.objects.filter(user=user)
    
#     return render(request, "profile.html", {"username": username, 'posts': posts})

@login_required
def dashboard(request):
    # user = User.objects.get(username = username)
    posts = Post.objects.all()
  
    return render (request, 'dashboard.html', {
         "posts": posts
        
    })


# @login_required
# class ProfileView(DetailView):
#     # model = Profile
#     template_name = "profile.html"

#     def get_context_data(self, *args, **kwargs):
#         user = User.objects.get(username = username)
#         context = super(ProfileView, self).get_context_data(*args, **kwargs)
#         posts = Post.objects.filter(user=user)
#         context['posts'] = posts

#         return context



# @method_decorator(login_required, name = 'dispatch')
# class CreateProfilePageView(LoginRequiredMixin, CreateView):
#     model = Profile
#     form_class = ProfilePageForm
#     template_name = 'create_profile.html'
#     # fields = ['bio',]
#     success_url = reverse_lazy('home')
    
    
#     def form_valid(self, form):
#         form.instance.user=self.request.user 
#         # return super().form_valid(form)
#         return super(CreateProfilePageView, self).form_valid(form)
#     success_url = '/'
   
    

# class ShowProfilePageView(DetailView):
#     model = User
#     template_name = 'profile.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
#         user_page = get_object_or_404(User, id = self.kwargs['pk'])
#         context["user_page"] = user_page
#         return context


@method_decorator(login_required, name='dispatch')
class UpdateProfileView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'update_profile.html'
    success_url = '/home'

    def get_object(self):
        return self.request.user

   
    
    