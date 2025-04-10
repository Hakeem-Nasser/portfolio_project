from django.urls import path
from . import views

app_name = 'blog'  # We'll still use 'blog' as the namespace

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),
]