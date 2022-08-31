
from dataclasses import fields
from django import forms
from .models import Customer
from .models import Account
from .models import Wallet

class CustomerRegistretionForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
class AccountRegistrationForm(forms.ModelForm):  
    class Meta:
        model=Account
        fields="__all__"    
        

