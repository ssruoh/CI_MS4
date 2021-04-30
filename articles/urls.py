from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('<article_id>', views.article_detail, name='article_detail'),
    path('add_article/', views.add_article, name='add_article'),
]
