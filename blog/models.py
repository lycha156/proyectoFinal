from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import validate_image_file_extension
from django.forms import DateField

class Post(models.Model):

    fechaPublicacion = models.DateField("Fecha de Publicacion", auto_now=False, auto_now_add=True)
    titulo = models.CharField("Titulo", max_length=50)
    articulo = models.TextField("Articulo")
    likes = models.IntegerField("Likes", default=0)
    fotoPortada = models.ImageField('Foto de Portada', upload_to ="fotos/articulos/", validators=[validate_image_file_extension], null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} (Publicado {self.fechaPublicacion})"


class Contacto(models.Model):

    nombre = models.CharField("Nombre y Apellido", max_length=100)
    email = models.EmailField("Email", max_length=254)
    mensaje = models.TextField("Mensaje")
    fecha = models.DateField("Fecha de Contacto", auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}, ({self.fecha}) - [{self.mensaje}]"
