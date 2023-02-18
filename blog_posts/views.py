from django.shortcuts import render


posts = [
    {
        'id': '1',
        'title': 'Django REST framework',
        'description': 'Django REST framework is a powerful and flexible toolkit for building Web APIs.'
    },
    {
        'id': '2',
        'title': 'Django Classed-based Views',
        'description': "Django's class-based views provide a object-oriented (OO) way of organizing your view code."
    },
    {
        'id': '3',
        'title': 'Django Signals',
        'description': "Django's signal dispatcher allows senders to notify receivers (or handlers) that an action "
                       "has occurred."
    }
]


def blog_posts(request):
    context = {'posts': posts}
    return render(request, 'blog_posts/blog_posts.html', context)


def blog_post(request, pk):
    post_obj = None
    for post in posts:
        if post['id'] == pk:
            post_obj = post
    context = {'post': post_obj}
    return render(request, 'blog_posts/blog_post.html', context)
