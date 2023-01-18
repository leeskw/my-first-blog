from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post


# path('', views.post_list, name='post_list'),
def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


# path('post/<int:pk>/', views.post_detail, name='post_detail'),
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    
    return render(request, 'blog/post_detail.html', context)
