from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
        
    return render(request, 'blog_index.html', context)

def about(request):
    return render(request, 'blog_about.html')

def contacto(request):
    return render(request, 'blog_contacto.html')

def page(request, id=id):
    post = get_object_or_404(Post, pk=id)

    context = {
        'post': post
    }

    return render(request, 'blog_page.html', context)