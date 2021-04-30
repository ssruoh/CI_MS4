from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


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
            'title': request.POST['post_code'],
            'description': request.POST['town_or_city'],
            'article_body': request.POST['county'],
            'image': request.POST['image'],
        }
        article_form = ArticleForm(article_form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, quantity in bag.items():
                product = Product.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                order_line_item.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(
                request, 'There was an issue with your form. \
                    Please recheck the fields.')

    return render(request, 'articles/add_article.html')
