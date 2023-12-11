from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django_blog.article.models import Article
from django.forms import ModelForm
from django.contrib import messages


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) < 2:
            self.add_error('name', 'Заголовок должен быть более 2 символов')
        if len(data) > 20:
            self.add_error('name', 'Заголовок должен быть не более 20 символов')
        return data

    def clean_body(self):
        data = self.cleaned_data['body']
        if len(data) < 2:
            self.add_error('body', 'Статья должна быть более 2 символов')
        if len(data) > 2000:
            self.add_error('body', 'Статья должна быть не более 2000 символов')
        return data


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно добавлена')
            return redirect('articles_index')
        messages.error(request, 'При добавлении статьи произошла ошибка')
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно обновлена')
            return redirect('articles_index')
        messages.error(request, 'При обновлении статьи произошла ошибка')
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        messages.success(request, 'Статья успешно удалена')
        return redirect('articles_index')
