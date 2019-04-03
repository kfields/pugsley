from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post

def index(request):
    posts = Post.objects.filter(last_published_at__lte=timezone.now()).order_by('last_published_at')
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post})

def user(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(owner=user)
    return render(request, 'blog/user.html', {'user': user, 'posts': posts})
