from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from blog.forms import PostForm

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


# path('post/new/', views.post_new, name='post_new'),
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm
    return render(request, 'blog/post_edit.html', {'form': form})


# path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
