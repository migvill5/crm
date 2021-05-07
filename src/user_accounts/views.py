from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'user_accounts/dashboard.html')


def contact(request):
    return render(request, 'user_accounts/contact.html')


def customers(request):
    return render(request, 'user_accounts/customers.html')
