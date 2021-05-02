from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product_review', 'product', 'reviewer', 'date')
    search_fields = ['product', 'product_review']


admin.site.register(Review, ReviewAdmin)
