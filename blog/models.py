from django.db import models
from django.core.validators import validate_image_file_extension

class Post(models.Model):

    fechaPublicacion = models.DateField("Fecha de Publicacion", auto_now=False, auto_now_add=True)
    titulo = models.CharField("Titulo", max_length=50)
    articulo = models.TextField("Articulo")
    likes = models.IntegerField("Likes", default=0)
    fotoPortada = models.ImageField('Foto de Portada', upload_to ="fotos/articulos/", validators=[validate_image_file_extension], null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} (Publicado {self.fechaPublicacion})"
