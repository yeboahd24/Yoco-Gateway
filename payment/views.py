from django.shortcuts import render
from django.conf import settings

from payment.models import Payment


def home(request):
    amount = Payment.objects.get(pk=1)
    return render(request, 'index.html', {'public_key': settings.TEST_PUBLIC_KEY, 'amount': amount})

