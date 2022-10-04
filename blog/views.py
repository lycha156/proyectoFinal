from django.shortcuts import render

def index(request):
    return render(request, 'blog_index.html')

def about(request):
    return render(request, 'blog_about.html')

def contacto(request):
    return render(request, 'blog_contacto.html')
