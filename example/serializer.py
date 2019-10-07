from rest_framework import routers, serializers
from django.contrib.auth.models import User


from example.models import Product

from example.models import Inventory
from example.models import Transaction

from example.models import Sale


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


class UseridSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id')

class ProductidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id')

class InventorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventory
        fields = ('__all__')

class InventoryidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id')

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ('__all__')

class SaleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sale
        fields = ('__all__')

