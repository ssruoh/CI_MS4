from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """
    Shopping bag page view
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add selected quantity of product to bag
    """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'{product.name} successfully added to bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """
    Update quantity of products in bag
    """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def delete_from_bag(request, item_id):
    """
    Delete item from bag
    """
    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
