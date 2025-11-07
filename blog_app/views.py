from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def index(request):
    post = Post.objects.order_by('-created_at')
    return render(request, 'blog_app/index.html', {'posts': post})

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('index')
    return render(request, 'blog_app/add_post.html')

