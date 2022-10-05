from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from wallet.models import Customer
from .serializers import CustomerSerializer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()  #request info
    serializer_class=CustomerSerializer   #type of Serializer

# Create your views here.
