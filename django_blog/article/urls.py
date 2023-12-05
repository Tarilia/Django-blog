from django.urls import path

from django_blog.article import views

urlpatterns = [
    path('', views.index),
]
