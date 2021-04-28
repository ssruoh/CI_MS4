from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article


def all_articles(request):
    """
    View to show all articles
    """
    articles = Article.objects.all().order_by('-date')

    context = {
        'articles': articles,
    }

    return render(request, 'articles/articles.html', context)


def article_detail(request, article_id):
    """
    View to show individual articles
    """
    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'articles/article_detail.html', context)
