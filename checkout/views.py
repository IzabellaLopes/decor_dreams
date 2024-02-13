"""Checkout Views"""

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OjNBYDpKS7Uim0j409PhFMgq8ZeVdjan0KJTfrPoBgdEs64tNtGZ5A7CCGnjDk9ci6kiGwgQTmIr9PORhnvb7Sw00mH2UZIDD',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)