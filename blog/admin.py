from django.contrib import admin
from .models import Post, Contacto

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = [
        'titulo',
        'articulo',
        'fotoPortada'
    ]

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    fields = [
        'nombre',
        'email',
        'mensaje'
    ]

    search_fields = ['nombre', 'email',]

