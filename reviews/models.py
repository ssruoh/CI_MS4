from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    review = models.TextField(max_length=250, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return f'Review by {self.reviewer}'
