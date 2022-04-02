from rest_framework import serializers
from .models import Customer, Orders

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['pk', 'name', 'email', 'created']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = ["order_number", "number_of_items", "cost", "customer_id"]