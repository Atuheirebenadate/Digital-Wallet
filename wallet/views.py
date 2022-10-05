from django.shortcuts import render
from requests import request

from wallet.models import Account, Card, Customer, Notifications, Receipt, ThirdParty, Transaction, Wallet
from .forms import CustomerRegistretionForm
from .forms import AccountRegistrationForm
from .forms import  WalletRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import ThirdpartyRegistrationForm
from .forms import NotificactionsRegistrationForm
from .forms import ReceiptRegistrationForm
# from . import forms
# import wallet

#customers
def register_customer(request):
    if request.method=="POST":
        form=CustomerRegistretionForm(request.POST)
        if form.is_valid():
            form.save
    else:
         form = CustomerRegistretionForm()
    return render(request,"wallet/register_customer.html",{"form":form})


#accounts
def register_account(request):
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save
    else:
         form = AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})
# wallet
def register_wallet(request):
  if request.method=="POST":  
     form=WalletRegistrationForm(request.POST)
     if form.is_valid():
        form.save
  else:
     form=WalletRegistrationForm()
  return render(request,"wallet/register_wallet.html",{"form":form})

def  register_transaction(request):
    if request.method=="POST":    
     form =TransactionRegistrationForm(request.POST)
     if form.is_valid():
        form.save
    else:
        form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})

def register_card(request):
    if request.method=="POST":
     form=CardRegistrationForm(request.POST)
    if form.is_valid():
        form.save
    else:
        form=CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form}) 

def register_Thirdparty(request):
    if request.method=="POST":
        form=ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save
        else:
          form=ThirdpartyRegistrationForm()
    return render(request,"wallet/register_Thirdparty.html",{"form":form}) 

def register_notification(request): 
    if request.method=="POST":  
      form=NotificactionsRegistrationForm(request.POST)
      if form.is_valid():
        form.save
    else:
        form=NotificactionsRegistrationForm() 
    return render(request,"wallet/register_notification.html",{"form":form})

def register_receipt(request):
    if request.method=="POST":
     form=ReceiptRegistrationForm(request.POST)
    if form.is_valid():
        form.save
    else:
        form=ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{form:form}) 
    

    # lists
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, "wallet/customers_list.html",{"customers":customers})

def list_account(request):
    accounts=Account.objects.all()
    return render(request, "wallet/account_list.html",{"accounts":accounts}) 

def list_card(request):
    cards=Card.objects.all()
    return render(request, "wallet/card_list.html",{"cards":cards})   

def list_notification(request):
    notifications=Notifications.objects.all()
    return render(request, "wallet/notification_list.html",{ "notification":notifications}) 

def list_receipt(request):
    receipt=Receipt.objects.all()
    return render(request, "wallet/receipt_list.html",{"receipt":receipt}) 

def list_thirdparty(request):
    thirdParty=ThirdParty.objects.all()
    return render(request, "wallet/thirdparty_list.html",{"thirdparty":thirdParty})


def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request, "wallet/wallet_list.html",{"wallets":wallets}) 

def list_transaction(request):
   transaction=Transaction.objects.all()
   return render(request, "wallet/transaction_list.html",{"transaction":transaction}) 

# def Customer_profile(request,id):
#     Customer=Customer.objects.get(id=id)
#     return render(request,"wallet/customer_profile.html,{"Customer":Customer}") 

# def edit_customer  (request,id):
#     Customer=Customer.objects.get(id=;id)
#    if request.method=="POST":
#     form=CustomerRegistretionForm(request.POST,)






# Create your views here.
