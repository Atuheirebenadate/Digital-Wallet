
from django.contrib import admin
# Register your models here.
from .models import Customer
from. models import Account
from.models import Wallet
from.models import Receipt
from.models import Reward
from.models import Notification
from.models import ThirdParty
from .models import Transaction
from.models import Card
from.models import Loan

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_name","account_number","balance",)
    search_fields=("account_name","account_number","balance",)
     
admin.site.register(Account, AccountAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("status","balance","time","transaction")
    search_fields=("satus","balance","time","transaction")
admin.site.register(Wallet,WalletAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","address")
    search_fields=("first_name","last_name","address")
admin.site.register(Customer,CustomerAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=("name","currency","amount")
    search_fields=("name","currency","amount")
admin.site.register(ThirdParty,ThirdPartyAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=("card_name","card_number","date")
    search_fields=("card_name","card_number","date")
admin.site.register(Card,CardAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt_type","file","date")
    search_fields=("receipt_type","file","date")
admin.site.register(Receipt,ReceiptAdmin) 

class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_amount","loan_intrest","due_date")
    search_fields=("loan_amount","loan_intrest","due_date")
admin.site.register(Loan,LoanAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_code","transaction_amount","transaction_number","date")
    search_fields=("transaction_code","transaction_amount","transaction_number","date")
admin.site.register(Transaction,TransactionAdmin) 

class RewardAdmin(admin.ModelAdmin):
    list_display=("reward_receipt","amount","date")
    search_fields=("reward_receipt","amount","date")
admin.site.register(Reward,RewardAdmin) 

class NotificationAdmin(admin.ModelAdmin):
    list_display=("title","massage","date")
    search_fields=("title","massage","date")
admin.site.register(Notification,NotificationAdmin)    


