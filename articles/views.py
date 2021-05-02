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
            https://stackoverflow.com/questions/8466768/using-request-user-with-django-modelform
            """
            article.author = request.user
            article.save()
            messages.success(request, 'Article added!')
            return redirect(reverse('article_detail', args=[article.id]))
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


@login_required
def edit_article(request, article_id):
    """
    View to edit an article
    """
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article_form_data = {
            'title': request.POST['title'],
            'description': request.POST['description'],
            'article_body': request.POST['article_body'],
            'image': request.POST['image'],
        }
        article_form = ArticleForm(
            article_form_data, instance=article)
        if article_form.is_valid():
            article_form.author = request.user
            article_form.save()
            messages.success(request, 'Article updated!')
            return redirect(reverse('article_detail', args=[article.id]))
        else:
            messages.error(
                request, 'There was a problem with the form. Please check the fields.')
    else:
        article = get_object_or_404(Article, pk=article_id)
        article_form = ArticleForm(instance=article)
        messages.info(
            request, 'You are editing an article.')

        template = 'articles/edit_article.html'

    context = {
        'article_form': article_form,
        'article': article,
    }

    return render(request, template, context)


@login_required
def delete_article(request, article_id):
    """
    View to delete article
    """
    article = get_object_or_404(Article, pk=article_id)
    if article.author == request.user:
        article.delete()
        messages.success(request, 'Article deleted!')
        return redirect(reverse('articles'))
    else:
        messages.info(
            request, "Only the original author or \
                administrator can delete articles.")
        return redirect(reverse('articles'))
