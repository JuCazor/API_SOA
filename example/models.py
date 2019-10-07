from django.db import models
from django.contrib.auth.models import User

# Create your views here.

class Example(models.Model):
    
    class Meta:
        db_table = "Example"


#modelo extra

class Product(models.Model):
    code = models.CharField(max_length=30, null=False, unique=True)
    name = models.CharField(max_length=30, default=False)
    description = models.CharField(max_length = 255, null = False)
    image = models.CharField(max_length=150, null=False)
    status = models.IntegerField(null=True)

    class Meta:
        db_table = "products"

class Inventory(models.Model):
    product_id= models.ForeignKey(Product, on_delete=models.SET(-1))
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.SET(-1))
    tax = models.FloatField(null=False)

    class Meta:
        db_table = "inventories"

class Transaction(models.Model):
    inventory_id = models.ForeignKey(Inventory, on_delete=models.SET(-1))
    date = models.DateField(null=False)
    typee = models.IntegerField(null=False)

    class Meta:
        db_table = "transactions"

class Sale(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET(-1))
    user_id = models.ForeignKey(User, on_delete=models.SET(-1))
    quantity = models.IntegerField(null=False)
    discount = models.FloatField(null=False )
    total = models.FloatField(null=False)
    date = models.FloatField(null=False)
    status = models.IntegerField(null=False)
    paymaneth_method=models.IntegerField(null=False)

    class Meta:
        db_table = "sales"

