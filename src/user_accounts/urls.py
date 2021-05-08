from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('customers/<str:pk>/', views.customers, name="customer"),
    path('products/', views.products, name="products"),
    path('create_order/', views.createOrder, name="create_order")
]
