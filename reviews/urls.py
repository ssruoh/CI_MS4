from . import views
from django.urls import path

urlpatterns = [
    path('review_product/<int:product_id>/',
         views.review_product, name='review_product'),
    path('delete_review/<int:review_id>/',
         views.delete_review, name='delete_review'),
]
