from django.urls import path
from django_blog.article.views import IndexView, ArticleView


urlpatterns = [
    path('', IndexView.as_view()),
    path('<str:tags>/<int:article_id>/', ArticleView.as_view(), name='article'),
]
