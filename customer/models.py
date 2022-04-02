from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField("name", max_length=240)
    email = models.EmailField(max_length=200)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_number = models.IntegerField(null=False, blank=False)
    number_of_items = models.IntegerField()
    cost = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_number

    