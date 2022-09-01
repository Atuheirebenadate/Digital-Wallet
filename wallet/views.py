from django.shortcuts import render
from .forms import CustomerRegistretionForm
from .forms import AccountRegistrationForm
from.forms import  WalletRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import ThirdpartyRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import ReceiptRegistrationForm

def register_customer(request):
    form = CustomerRegistretionForm()
    return render(request,"wallet/register_customer.html",{"form":form})
def register_account(request):
    form = AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})
def register_wallet(request):
    form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form})
def  register_transaction(request):
    form =TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})  
def register_card(request):
    form=CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form})  
def register_Thirdparty(request):
    form=ThirdpartyRegistrationForm()
    return render(request,"wallet/register_Thirdparty.html",{"form":form}) 
def register_notification(request):  
    form=NotificationRegistrationForm() 
    return render(request,"wallet/register_notification.html",{"form":form})
def register_receipt(request):
    form=ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{form:form})    



# Create your views here.
