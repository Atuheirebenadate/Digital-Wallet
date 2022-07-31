# import email
# from pyexpat import model
# from statistics import model
# from datetime import date
# from pyexpat import model

from django.db import models
# from django.forms import DateField

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=12)
    address=models.TextField()
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    age=models.PositiveIntegerField()

class Account(models.Model):
        account_number=models.IntegerField()
        account_name=models.CharField(max_length=15)
        balance=models.IntegerField()
        # wallet=models.ForeignKey()
        # accountType=models.ForeignKey()

class Wallet(models.Model): 
    status=models.CharField(max_length=15)
    transaction=models.CharField(max_length=15)
    time=models.CharField(max_length=15)
    balance=models.IntegerField()

class Transaction(models.Model):
    transaction_code=models.CharField(max_length=15)
    transaction_amount=models.IntegerField()
    transaction_number=models.IntegerField()
    date=models.DateTimeField()
    # time=models.DateTimeField()

class Card(models.Model):
       card_name=models.CharField(max_length=15)
       card_number=models.IntegerField()
       date=models.DateTimeField()

class ThirdParty(models.Model):
        name=models.CharField(max_length=15)
        currency=models.IntegerField()
        amount=models.IntegerField()

class Notification(models.Model):
            title=models.CharField(max_length=15)
            massage=models.CharField(max_length=15)
            date=models.DateTimeField()

class Receipt(models.Model):
         receipt_type=models.CharField(max_length=15)
         file=models.FileField()
         date=models.DateTimeField()

class Loan(models.Model):
    loan_amount=models.IntegerField()
    loan_intrest=models.IntegerField()
    due_date=models.DateTimeField()

class Reward(models.Model):
    reward_receipt=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField()    




