from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article
from django.db.models import Count


def main_page(request):
    """ Dashboard function returns a template with subjects and tasks from DB based on user """
    articles = Article.objects.all().order_by('-id')
    return render(request, 'campus_app/main.html', context={'articles': articles})


@login_required()
def articles_by_user_page(request):
    """ Dashboard function returns a template with subjects and tasks from DB based on user """
    user_articles = Article.objects.filter(user=request.user)
    all_types = [choice[0] for choice in Article.type.field.choices]

    # Запит до бази даних для підрахунку кількості робіт по кожному типу
    result = (
        user_articles
        .values('type')
        .annotate(total=Count('type'))
    )

    # Створення словника з результатів запиту, де відсутнім типам робіт буде призначено значення 0
    result_arr = []
    result_dict = {item['type']: item['total'] for item in result}
    for article_type in all_types:
        result_arr.append(result_dict.get(article_type, 0))

    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles_by_user')
        else:
            messages.error(request, f'Виникла помилка під час створення, спробуйте ще раз: \n{form.errors}')

    context = {'articles': user_articles, 'count_types': result_arr,
               'form': form}
    return render(request, 'campus_app/articles_by_user.html', context=context)


@login_required()
def edit_article_page(request, article_id):
    """ Subject function returns a template with subjects and tasks from DB based on user """
    article = Article.objects.filter(id=article_id, user=request.user).first()

    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles_by_user')
        else:
            messages.error(request, f'Виникла помилка під час редагування, спробуйте ще раз\n{form.errors} ')
    return render(request, 'campus_app/edit_article.html', {'form': form, 'article': article})


@login_required()
def delete_article(request, article_id):
    """ Dashboard function returns a template with subjects and tasks from DB based on user """
    article = Article.objects.filter(id=article_id, user=request.user).first()
    if article:
        article.delete()
        return redirect('articles_by_user')
    else:
        return redirect('articles_by_user')
