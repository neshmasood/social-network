from django.urls import path
from . import views 




# urlpatterns = [
#     path('', views.DonationPage.as_view(), name='donation'),
#     # path('', views.index, name="index"),
#     # path('charge/', views.charge, name="charge"),
    
       
    
# ]

from payments.views import CancelView, SuccessView, CreateCheckoutSessionView

urlpatterns = [
    path('', views.DonationPage.as_view(), name='donation'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]