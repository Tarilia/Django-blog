from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', args=['python', 42]))


class ArticleView(View):
    def get(self, request, tags, article_id):
        return render(request, 'articles/index.html',
                      context={'article_id': article_id, 'tags': tags})
