from . import views
from django.urls import path

urlpatterns = [
    path('<int:product_id>/', views.review_product, name='review_product'),
]
