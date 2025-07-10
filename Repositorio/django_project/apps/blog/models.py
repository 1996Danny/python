from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# modelo de categorias

# modelo de comentarios(usuario que comenta y post al que comenta el usuario)

class Post(models.Model):
    # OneToOneField (1:1)
    # ManyToManyField (M:N) orm encarga de crear la tabla intermedia
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120, null=False, blank=False, verbose_name="Título") 
    contenido = models.TextField(verbose_name="Contenido del Post")
    imagen = models.ImageField(null=True, blank=True, upload_to="media/posts")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-fecha_creacion"]