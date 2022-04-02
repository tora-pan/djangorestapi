from django.shortcuts import render
from .models import Customer, Orders
from rest_framework import generics
from .serializers import CustomerSerializer, OrderSerializer


# CUSTOMERS

class CustomerCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Customer.objects.all(),
    serializer_class = CustomerSerializer

class CustomerList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# ORDERS

class OrderCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Orders.objects.all(),
    serializer_class = OrderSerializer


class OrderList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer