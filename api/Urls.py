from django.urls import path,include
from rest_framework import routers
from wallet.models import Customer
from .views import CustomerViewSet
router=routers.DefaultRouter()
router.register(r'customers',CustomerViewSet,basename=Customer)
urlpatterns=[
      path("",include(router.urls)),
]