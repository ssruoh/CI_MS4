from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib.auth.models import User
from .models import Review
from .forms import ReviewForm
from django.contrib import messages

# Create your views here.


@login_required
def review_product(request, product_id):
    """
    View to add a review to a product,
    adjusted from https://www.youtube.com/watch?v=pNVgLDKrK40
    """
    product = get_object_or_404(Product, pk=product_id)
    user_review = None
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            user_review = review_form.save(commit=False)
            user_review.product = product
            user_review.reviewer = request.user
            user_review.save()
            messages.success(request, 'Review added!')
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()
    return render(request, 'product_detail.html', {'product_id': product_id, 'review_form': review_form})
