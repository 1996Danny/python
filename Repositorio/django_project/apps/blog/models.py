from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# modelo de categorias

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["id"]
    

class Post(models.Model):
    # OneToOneField (1:1)
    # ManyToManyField (M:N) orm encarga de crear la tabla intermedia
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120, null=False, blank=False, verbose_name="Título") 
    contenido = models.TextField(verbose_name="Contenido del Post")
    imagen = models.ImageField(null=True, blank=True, upload_to="media/posts")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-fecha_creacion"]

# modelo de comentarios(usuario que comenta y post al que comenta el usuario)
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios") # a que post pertenece el comentario
    autor = models.ForeignKey(User, on_delete=models.CASCADE) # a que usuario pertenece el comentario
    contenido = models.TextField(verbose_name="Comentario")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username}"
    
    class Meta:
        db_table = "comentarios"
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-fecha_creacion"] 

