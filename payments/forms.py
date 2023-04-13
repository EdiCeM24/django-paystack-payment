from django import forms
from . import PaymentForm

from .models import Payment

class Payment():
    pass



class PaymentForm(forms.ModelForm):
    class Meta:
        model =  Payment
        field = ("amount", "email") 