from django import forms
from .models import Review


class ReviewForm(form.modelForm):
    class Meta:
        model = Review
        fields = ('product_review',)
        exclude = ('reviewer',)

        widgets = {
            'product_review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a review!', 'rows': '3'})
        }
