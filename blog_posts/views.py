from django.http import HttpResponse
from django.shortcuts import render


def blog_posts(request):
    return render(request, 'blog_posts/blog_posts.html')


def blog_post(request, pk):
    return render(request, 'blog_posts/blog_post.html')
