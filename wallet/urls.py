
# from django.urls import path
# from .views import register_Thirdparty, register_account, register_card, register_customer, register_notification, register_receipt, register_transaction, register_wallet
# from wallet import views

from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path("wallet/",include("wallet.urls")),#signifies another url
    path('admin/', admin.site.urls),
    path('api/',include("api.urls")),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    


    
# path("register/",register_customer, name="registration" ),
# path("register2/",register_account, name="account"),
# path("register3/", register_wallet,name="wallet"),
# path("register4/", register_transaction, name="transaction"),
# path("register5/",register_card, name="card"),
# path("register6/", register_Thirdparty, name="thirdparty"),
# path("register7/",register_notification, name="notification"),
# path("register8/",register_receipt,name="receipt"),
# path("customers/",views.list_customers,name="Customer"),
# path("accounts/",views.list_account,name="account"),
# path("wallet/",views.list_wallet,name="wallet"),
# path("transaction/",views.list_transaction,name="trascaction"),
# path("cards/",views.list_card,name="card"),
# path("thirdparty/",views.list_thirdparty,name="Thirdparty"),
# path("notifications/",views.list_notification,name="notifications"),
# path("receipt/",views.list_receipt,name="receipt"),
# path("customers/<int:id>/",views.Customer_profile,{{Customer.first_name}} {{customer.last_name}}name="Customer"),
# ]