from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import FormContacto
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        postsObjects = Post.objects.filter( Q(titulo__contains = query) | Q(fechaPublicacion__contains = query))[:25]
    else:
        posts = Post.objects.all()

        pagination = Paginator(posts, 2)
        page_number = request.GET.get('page')
        postsObjects = pagination.get_page(page_number)

    context = {
        'posts': postsObjects,
    }
        
    return render(request, 'blog_index.html', context)

def about(request):
    return render(request, 'blog_about.html')

def contacto(request):
    form = FormContacto()

    if request.method == 'POST':
        form = FormContacto(request.POST)
        
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Mensaje enviado con exito')
                return redirect('blog_contacto')
            else:
                messages.warning('Error al enviar el mensaje.')
                return render(request, 'blog_contacto.html', context = {'form': form})
        except Exception as e:
            messages.warning(f'Error al enviar el mensaje. Detalle del error: {e}')
            return redirect('blog_contacto')
    
    context = {
        'form': form
    }
    return render(request, 'blog_contacto.html', context)

def page(request, id=id):
    post = get_object_or_404(Post, pk=id)

    context = {
        'post': post
    }

    return render(request, 'blog_page.html', context)