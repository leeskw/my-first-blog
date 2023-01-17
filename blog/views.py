from django.shortcuts import render


# path('', views.post_list, name='post_list'),
def post_list(request):
    return render(request, 'blog/post_list.html', {})
