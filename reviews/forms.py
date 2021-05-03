from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('product_review',)
        exclude = ('reviewer',)

        widgets = {
            'product_review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a review!', 'rows': '3'})
        }
