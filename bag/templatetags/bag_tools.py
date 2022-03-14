""" Template tags to calculate subtotal in shopping bag """

from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Function to return price * ammount of products"""
    return price * quantity
