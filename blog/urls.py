from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blog_index"),
    path('about', views.about, name="blog_about"),
    path('contacto', views.contacto, name="blog_contacto"),
]
