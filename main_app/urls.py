from django.urls import path
from . import views
from .views import PostDetailView

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/new/', views.PostCreate.as_view(), name="post_create"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    
    
    
            
]