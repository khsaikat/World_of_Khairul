from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog_posts'),
    path('<str:pk>/', views.blog_post, name='blog_post'),
]
