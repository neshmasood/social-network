
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.conf import settings
# from django.urls import reverse
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views import View
import stripe
# from main_app.models import Price, Product
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


class DonationPageView(TemplateView):
    template_name = "donation.html"
    
    def get_context_data(self, **kwargs):
        context = super(DonationPageView, self).get_context_data( **kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
      
        return context 
    

def success(request):
    if request.method == "POST":
        return redirect("success/")
    else:
        return render (request, 'payments/donation.html')
    
@login_required
def checkout(request):
    if request.method == "POST":
        return redirect("success/")
    else:
        return render (request, 'payments/donation.html')
    
    # def SuccessView(request):
    #     return render(request, 'payments/success')
# class SuccessView(TemplateView):
#         template_name = "payments/success.html"
#         success_url = 'success.html'
       


# class CancelView(TemplateView):
#     template_name = "cancel.html"
    
   
    
    # def Charge(request):
    #     if request.method == 'POST':
    #         charge = stripe.Charge.create(
    #             amount = 1000,
    #             currency = 'usd',
    #             description = 'A donation charge',
    #             source=request.POST['stripeToken'],  
    #         )
          
    #         return render('charge.html')
    
    
    
    
    
  



