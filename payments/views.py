from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
import stripe


stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY

# Create your views here.




class DonationPage(TemplateView):
    template_name = 'donation.html'
    
    
    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context 
    
    

    # def Charge(request):
    #     if request.method == 'POST':
    #         charge = stripe.Charge.create(
    #             amount = 1000,
    #             currency = 'usd',
    #             description = 'A donation charge',
    #             source = request.POST['stripeToken'],  
    #         )
          
    #         return render(request, 'charge.html')
    
    
    
    # def donation(request):
    #     stripe.api_key = settings.STRIPE_SECRET_KEY
        
    #     session = stripe.checkout.Session.create(
    #         payment_method_types=['card'],
    #         line_items=[
    #             {
    #                 'price': 'price_1KqrZYFLN4dlqlUtEm4oriEH',
    #                 'quantity': 1,
    #             },
    #         ],
    #         mode='payment',
    #         success_url= request.build.absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
    #         cancel_url= request.build.absolute_uri(reverse('donation')),
    #     )
        
    #     context = {
    #         'session_id': session.id,
    #         'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    #     }
    #     return render(request, 'donation')
        
    
    # def success(request):
    #     return render(request, 'success')



