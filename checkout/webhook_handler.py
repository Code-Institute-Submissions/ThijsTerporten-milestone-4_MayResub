""" WEBHOOK handler class """

from django.http import HttpResponse


class StripeWhHandler:
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle payment intent succeeded """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """ Handle payment_failed webhook """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)