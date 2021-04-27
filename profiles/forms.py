from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


def __init__(self, *args, **kwargs):
    """
    Add placeholders, set autofocus on Phone number on page load and remove form
    labels
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        'default_phone_number': 'Phone Number',
        'default_street_address': 'Street Address',
        'default_post_code': 'Postal Code',
        'default_town_or_city': 'Town/City',
        'default_county': 'County',
    }

    self.fields['default_phone_number'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if field != 'default_country':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].label = False
