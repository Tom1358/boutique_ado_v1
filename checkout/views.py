from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    temmplate = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jxx0EAzKTdG4q4tFocyLGk5nNVXe4UklJMt62XRg92sttHRcaM4NveqTXll7BkxdsvgQz0soPKsszPnfYtHfpO400NG12ND9m',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
