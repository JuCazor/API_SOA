from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404



#IsAuthenticated


from example.models import Product

from example.models import Transaction
from example.models import Sale

from example.models import Inventory


from example.serializer import UserSerializer
from example.serializer import ProductSerializer
from example.serializer import UseridSerializer
from example.serializer import ProductidSerializer
from example.serializer import InventorySerializer
from example.serializer import InventoryidSerializer
from example.serializer import TransactionSerializer
from example.serializer import SaleSerializer


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class ProductsList(APIView):
    
    def get(self, request, format=None):
        queryset = Product.objects.filter(status = 1)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        postProduct = Product.objects.create(
            code = request.data['code'],
            name = request.data['name'],
            description = request.data['description'],
            image = request.data['image'],
            status = request.data['status']
        )
        postProduct.save()
        id = request.data['user_id']
        postInventario = Inventory.objects.create(
            quantity = request.data['quantity'],
            price = request.data['price'],
            tax = request.data['tax'],
            product_id = postProduct,
            user_id = User.objects.get(pk=id)
        )
        postTransaction = Transaction.objects.create(
            date = request.data['date'],
            typee = 1,
            inventory_id = postInventario
        )
        postTransaction.save()
        postInventario.save()
        return Response(postInventario.id)

class ProductListAll(APIView):
    def get(self, request, format=None):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ProductSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Product.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ProductSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CancelSale(APIView):
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            venta = Sale.objects.get(pk=id)
            venta.status = 0
            venta.save()
            inventario = Inventory.objects.get(product_id = venta.product_id)
            inventario.quantity = inventario.quantity + venta.quantity
            inventario.save()
            return Response('Guardado')

class UsersList(APIView):
    
    def get(self, request, format=None):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = User.objects.create_user(request.data)
            user.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = UserSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        User.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = UserSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class InventoriesList(APIView):
    
    def get(self, request, format=None):
        queryset = Inventory.objects.all()
        serializer = InventorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = InventorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class InventoriesDetail(APIView):
    def get_object(self, id):
        try:
            return Inventory.objects.get(pk=id)
        except Inventory.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = InventorySerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Inventory.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = InventorySerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class TransactionsList(APIView):
    
    def get(self, request, format=None):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TransactionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class TransactionDetail(APIView):
    def get_object(self, id):
        try:
            return Transaction.objects.get(pk=id)
        except Transaction.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = TransactionSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Transaction.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = TransactionSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SalesList(APIView):
    
    def get(self, request, format=None):
        queryset = Sale.objects.all()
        serializer = SaleSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        id = request.data['product_id']
        inventario = Inventory.objects.get(product_id = id)
        cantidad = request.data['quantity']
        cantidadD = inventario.quantity
        print(cantidad)
        print(cantidadD)
        if int(cantidadD) - int(cantidad) >= 0:
            venta = Sale.objects.create(
                quantity = cantidad,
                discount = request.data['discount'],
                total = request.data['total'],
                date = request.data['date'],
                status = request.data['status'],
                payment_method = request.data['payment_method'],
                product_id = Product.objects.get(pk = id),
                user_id = User.objects.get(pk=request.data['user_id'])
            )
            inventario.quantity = int(cantidadD) - int(cantidad)
            inventario.save()
            venta.save()
            transaccion =Transaction.objects.create(
                date = request.data['date'],
                typee = 2,
                inventory_id = inventario
            ) 
            transaccion.save()
            return Response('exitoso')
        return Response('error')

class SaleDetail(APIView):
    def get_object(self, id):
        try:
            return Sale.objects.get(pk=id)
        except Sale.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = SaleSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Sale.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = SaleSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


