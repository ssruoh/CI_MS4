from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('add_article/', views.add_article, name='add_article'),
    path('<article_id>/', views.article_detail, name='article_detail'),
    path('edit_article/<article_id>/', views.edit_article, name='edit_article'),
    path('delete_article/<article_id>',
         views.delete_article, name='delete_article'),
]
