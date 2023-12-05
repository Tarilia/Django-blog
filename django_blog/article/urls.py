from django.urls import path
from django_blog.article.views import IndexView


urlpatterns = [
    path('', IndexView.as_view()),
]
