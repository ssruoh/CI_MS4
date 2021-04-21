from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    # Stops users from manually accessing /checkout
    if not bag:
        messages.error(request, 'You have nothing in your bag!')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IasCvIaCMmNhIfzGIPwQ3wzNsH57WNDtKYNB8wH6MStYeJ7dk9SHCno80yKuibx8UQiBJyMeXz6ujtvpu4qdShq00AD1tLyKK',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
