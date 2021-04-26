from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    Model that allows saving delivery details and displaying order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=32, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country *', null=True, blank=True)
    default_post_code = models.CharField(max_length=32, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=32, null=True, blank=True)
    default_street_address = models.CharField(
        max_length=100, null=True, blank=True)
    default_county = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create/update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Save profile if user already exists
    instance.userprofile.save()
