from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'street_address',
                  'town_or_city', 'post_code', 'country', 'county',)


def __init__(self, *args, **kwargs):
    """
    Add placeholders, set autofocus on Full Name on page load and remove form
    labels
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        'full_name': 'Full Name',
        'email': 'Email',
        'phone_number': 'Phone Number',
        'street_address': 'Street Address',
        'post_code': 'Postal Code',
        'town_or_city': 'Town/City',
        'county': 'County',
        'country': 'Country',
    }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].label = False
