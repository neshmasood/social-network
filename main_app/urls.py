from django.urls import path
from django.contrib import admin
from . import views 
from .views import PostDetailView, DeletePostView, UpdatePostView, AddCommentView, LikeView
from payments.views import DonationPageView, SuccessView



urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/new/', views.PostCreate.as_view(), name="post_create"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('posts/<int:pk>/delete', DeletePostView.as_view(), name="post_delete"),
    path('posts/<int:pk>/update', UpdatePostView.as_view(), name="post_update"),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="comment_add"),
    path('like/<int:pk>', LikeView, name="like_post"),
   
    # path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', DonationPageView.as_view(), name='donation'),
    # path('charge/', views.Charge, name="charge"),
    # path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    
    
    
            
]