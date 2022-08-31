from django.shortcuts import render
from .forms import CustomerRegistretionForm
from .forms import AccountRegistrationForm

def register_customer(request):
    form = CustomerRegistretionForm()
    return render(request,"wallet/register_customer.html",{"form":form})
def register_account(request):
    form = AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})


# Create your views here.
