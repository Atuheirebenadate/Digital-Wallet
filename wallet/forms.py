
from django import forms
from .models import Customer 
from .models import Account
from .models import Wallet
from .models import Transaction
from .models import Card
from .models import Notifications
from .models import Receipt
from .models import ThirdParty

class CustomerRegistretionForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class AccountRegistrationForm(forms.ModelForm):  
    class Meta:
        model=Account
        fields = "__all__"  
              
class WalletRegistrationForm(forms.ModelForm):  
    class Meta:
        model = Wallet
        fields = "__all__"  
class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model =Transaction
        fields="__all__"   
class CardRegistrationForm(forms.ModelForm): 
    class Meta:
        model=Card
        fields="__all__"  
class ThirdpartyRegistrationForm(forms.ModelForm):
    class Meta:
        model=ThirdParty
        fields="__all__"  
class NotificactionsRegistrationForm(forms.ModelForm):
    class Meta:
        model=Notifications
        fields="__all__"
class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:
        model=Receipt
        fields="__all__"  


