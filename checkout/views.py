""" Checkout View """

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe
from bag.contexts import bag_contents
from .forms import OrderForm


def checkout(request):
    """ Checkout function """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in the bag!")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KT6XyKSWQ8RQNHSjSvlSnaTRk39FbxXfm8EXmey0pUz7zBVCiPfHRC5aE6daAZig3fG5g7QCzrPTX8hg9hiilwr00me3B8LaF',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
