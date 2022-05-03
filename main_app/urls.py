from django.urls import path
# from django.contrib import admin
from . import views 
from .views import PostDetailView, DeletePostView, UpdatePostView, PostCreateView, AddCommentView, LikeView, UpdateProfileView
from payments.views import DonationPageView
from main_app.views import dashboard



urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/new/', PostCreateView.as_view(), name="post_create"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('posts/<int:pk>/delete', DeletePostView.as_view(), name="post_delete"),
    path('posts/<int:pk>/update', views.UpdatePostView.as_view(), name="post_update"),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name="comment_add"),
    #  path('comment/new', AddCommentView.as_view(), name="comment_add"),
    path('like/<int:pk>', LikeView, name="like_post"),
   
    # path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', DonationPageView.as_view(), name='donation'),
    # path('charge/', views.Charge, name="charge"),
    # path('cancel/', CancelView.as_view(), name='cancel'),
    # path('success/', views.success.as_view(), name='success'),
    path('user/<username>/', views.profile, name='profile'),
    # path('user/<username>/', ProfileView, name='profile'),
    path('profile/update/<int:pk>/', UpdateProfileView.as_view(), name='update_profile'),
    # path('user/<int:pk>/', ShowProfilePageView.as_view(), name = 'profile'),
    # path('profile/create/', views.CreateProfilePageView.as_view(), name = 'create_profile'),
    path('dashboard/', dashboard, name="dashboard"),
     
            
]