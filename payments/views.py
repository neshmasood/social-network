from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.urls import reverse
import stripe


stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY

# Create your views here.




class DonationPage(TemplateView):
    template_name = 'donation.html'
    
    
    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context 
    
    

        

