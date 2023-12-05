from django.contrib import admin
from django.urls import path, include
from django_blog import views
from django_blog.views import IndexPageView


urlpatterns = [
    path('', IndexPageView.as_view(template_name='index.html')),
    path('about/', views.about),
    path('articles/', include('django_blog.article.urls')),
    path('admin/', admin.site.urls),
]
