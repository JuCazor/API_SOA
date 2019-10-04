from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from example import views

urlpatterns = [
  
     re_path(r'^products_list/$', views.ProductsList.as_view() ),
     re_path(r'^product_detail/(?P<id>\d+)$', views.ProductDetail.as_view() ),
     
     re_path(r'^users_list/$', views.UsersList.as_view() ),
     re_path(r'^user_detail/(?P<id>\d+)$', views.UserDetail.as_view() ),
     
     re_path(r'^invetories_list/$', views.InventoriesList.as_view() ),
     re_path(r'^inventory_detail/(?P<id>\d+)$', views.InventoriesDetail.as_view() ),

     re_path(r'^transaccions_list/$', views.TransactionsList.as_view() ),
     re_path(r'^transaccion_detail/(?P<id>\d+)$', views.TransactionDetail.as_view() ),

     re_path(r'^sales_list/$', views.SalesList.as_view() ),
     re_path(r'^sale_detail/(?P<id>\d+)$', views.SaleDetail.as_view() ),
]