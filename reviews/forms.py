from django import forms
from .models import Review


class ReviewForm(form.modelForm):
    class Meta:
        model = Review
        fields = ('review',)
        exclude = ('reviewer',)

        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a review!', 'rows': '3'})
        }
