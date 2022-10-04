from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="blog_index"),
    path('about', views.about, name="blog_about"),
    path('contacto', views.contacto, name="blog_contacto"),
    path('page/<int:id>', views.page, name="blog_page"),
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
