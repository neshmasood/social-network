from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.conf import settings
# from django.urls import reverse
# from django.http import JsonResponse
from django.views import View
import stripe
from main_app.models import Price, Product


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

class CreateCheckoutSessionView(View):
    
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs['pk'])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.BASE_URL + '/payments/success/',
            cancel_url=settings.BASE_URL + '/payments/cancel/',
        )
        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class DonationPage(TemplateView):
    template_name = 'donation.html'
    
    
    def get_context_data(self, *args, **kwargs):
        product = Product.objects.get(name="Donation")
        prices = Price.objects.filter(product=product)
        context = super(DonationPage, self).get_context_data(*args, **kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
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



