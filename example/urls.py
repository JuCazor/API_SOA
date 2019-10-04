from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from example import views

urlpatterns = [
  
     re_path(r'^lista_productos/$', views.ProductsList.as_view() ),
     re_path(r'^detalle_producto/(?P<id>\d+)$', views.ProductDetail.as_view() ),
     
     re_path(r'^users_lista/$', views.UsersList.as_view() ),
     re_path(r'^users_detail/(?P<id>\d+)$', views.UserDetail.as_view() ),
     
     re_path(r'^inventario_lista/$', views.InventoriesList.as_view() ),
     re_path(r'^inventario_detail/(?P<id>\d+)$', views.InventoriesDetail.as_view() ),

     re_path(r'^transaccion_lista/$', views.TransactionsList.as_view() ),
     re_path(r'^transaccion_detail/(?P<id>\d+)$', views.TransactionDetail.as_view() ),

     re_path(r'^sales_lista/$', views.SalesList.as_view() ),
     re_path(r'^sales_detail/(?P<id>\d+)$', views.SaleDetail.as_view() ),
]