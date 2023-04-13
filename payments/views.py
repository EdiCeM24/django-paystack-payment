from django.shortcuts import render
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .import forms
from django.contrib import messages
from django.conf import settings
from .models import Payment

# Create your views here.
def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'make_payment.html', {'payment': payment})
    else: 
        payment_form = forms.PaymentForm()
    return render(request, 'initiate_payment.html', {'payment_form': payment_form})

def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    Payment = get_object_or_404(Payment, ref=ref)
    verified = Payment.verify_payment()
    if verified:
        messages.success(request, 'verification Successful.')
    else:
        messages.error(request, 'verification failed.')
    return redirect('initiate-payment')