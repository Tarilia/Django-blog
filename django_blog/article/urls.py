from django.urls import path
from django_blog.article.views import IndexView, ArticleView


urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view()),
]
