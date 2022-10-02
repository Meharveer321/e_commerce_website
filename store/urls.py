from django.urls import path
from . import views

urlpatterns=[
    path('', views.Store, name="Store"),
    path('Cart/', views.Cart, name="Cart"),
    path('Checkout/', views.Checkout, name="Checkout"),
    path('update_item/', views.updateItem, name="update_item"),
]