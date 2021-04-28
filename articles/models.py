from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    article_body = models.CharField(max_length=4000, null=False, blank=False)
    description = models.CharField(
        max_length=100, null=False, blank=False)
    image = models.URLField(max_length=200, null=False, blank=False)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
