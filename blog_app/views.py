from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
# Create your views here.

def index(request):
    post = Post.objects.order_by('-pub_date')
    return render(request, 'blog_app/index.html', {'posts': post})

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')

        if title and author and content:
            Post.objects.create(
                title=title,
                author=author,
                content=content,
                pub_date=timezone.now()
            )
            return redirect('blog-app-index')  

    return render(request, 'blog_app/add_post.html')
