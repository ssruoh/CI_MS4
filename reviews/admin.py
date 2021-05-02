from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'product', 'reviewer', 'date')
    search_fields = ['product', 'review']


admin.site.register(Review, ReviewAdmin)
