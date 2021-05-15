from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import OrderForm, CustomerForm
from .filters import OrderFilter


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers, 
    'total_orders': total_orders, 'delivered': delivered, 
    'pending': pending}

    return render(request, 'user_accounts/dashboard.html', context )


def contact(request):
    return render(request, 'user_accounts/contact.html')


def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 'order_count': order_count,
    'myFilter': myFilter}
    return render(request, 'user_accounts/customers.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'user_accounts/products.html', {'products': products})

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        # Procedute to save data in a POST
        formset = OrderFormSet(request.POST, isinstance=customer)
        if formset.is_valid():
            formset.save()
            return redirect(('/'))

    context = {'formset': formset}
    return render(request, 'user_accounts/order_form.html', context)

def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        # Procedure to save data in a POST for not new data
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect(('/'))

    context = {'form': form}
    return render(request, 'user_accounts/order_form.html', context) 


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'user_accounts/delete.html', context)


def createCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':
        # Procedute to save data in a POST
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(('/'))

    context = {'form': form}
    return render(request, 'user_accounts/customer_form.html', context)

def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    context = {'form': form}

    return render(request, 'user_accounts/customer_form.html', context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect(('/'))

    context = {'form': form}
    return render(request, 'user_accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'user_accounts/login.html', context)