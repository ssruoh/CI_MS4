from django.shortcuts import render
from django.views import generic
from .models import Article


def all_articles(request):
    """
    View to show all products
    """
    articles = Article.objects.all().order_by('-date')

    context = {
        'articles': articles,
    }

    return render(request, 'articles/articles.html', context)


"""
# Adapted from https://djangocentral.com/building-a-blog-application-with-django/
class ArticleList(generic.ListView):
    queryset = Article.objects.order_by('-date')
    template_name = 'articles.html'


class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'article_details.html'
"""
