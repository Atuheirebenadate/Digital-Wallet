
from django.urls import path
from .views import register_Thirdparty, register_account, register_card, register_customer, register_notification, register_receipt, register_transaction, register_wallet

urlpatterns = [
path("register/",  register_customer, name="registration" ),
path("register2/", register_account, name="account"),
path("register3/", register_wallet,name="wallet"),
path("register4/", register_transaction, name="transaction"),
path("register5/",register_card, name="card"),
path("register6/", register_Thirdparty, name="thirdparty"),
path("register7/",register_notification, name="notification"),
path("register8/",register_receipt,name="receipt"),
]