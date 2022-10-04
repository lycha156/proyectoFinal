from django.shortcuts import render
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
    pass