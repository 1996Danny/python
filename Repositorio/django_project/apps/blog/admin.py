from django.contrib import admin

from .models import Post, Categoria, Comentario

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ["titulo", "fecha_creacion", "autor"]


admin.site.register(Categoria)
admin.site.register(Comentario)