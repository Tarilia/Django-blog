from django.urls import path
from django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView


urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view()),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
