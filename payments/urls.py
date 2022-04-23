from django.urls import path
from . import views 




urlpatterns = [
    path('', views.DonationPage.as_view(), name='donation'),
       
    
]