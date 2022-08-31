from django.urls import path
from .views import register_account, register_customer

urlpatterns = [
path("register/",register_customer, name="registration" ),
path("register2/",register_account, name="account"),
]