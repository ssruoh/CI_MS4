from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.contrib import messages


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


@login_required
def add_article(request):
    """
    View to add an article
    """
    if request.method == 'POST':
        article_form_data = {
            'title': request.POST['title'],
            'description': request.POST['description'],
            'article_body': request.POST['article_body'],
            'image': request.POST['image'],
        }
        article_form = ArticleForm(article_form_data)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            """ Use request.user to attach current user as author of article,
            https://stackoverflow.com/questions/19799941/attaching-a-current-user-object-to-django-form
            """
            article.author = request.user
            article.save()
            return redirect(reverse('add_article'))
        else:
            messages.error(
                request, 'There was a problem with the form. Please check the fields.')
    else:
        article_form = ArticleForm()
        template = 'articles/add_article.html'

        context = {
            'article_form': article_form,
        }
        return render(request, template, context)
