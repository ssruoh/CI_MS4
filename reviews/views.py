from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib.auth.models import User
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


@login_required
def review_product(request, product_id):
    """
    View to add a review to a product,
    adjusted from https://www.youtube.com/watch?v=pNVgLDKrK40
    """
    product = get_object_or_404(Product, pk=product_id)
    # redirect_url used as recommended by https://github.com/Tmuat
    redirect_url = request.POST.get("redirect_url")
    user_review = None
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        user_review = review_form.save(commit=False)
        user_review.product = product
        user_review.reviewer = request.user
        user_review.save()
        messages.success(request, 'Review added!')
        return redirect(redirect_url)
