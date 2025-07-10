from django.shortcuts import render
from django.http import HttpResponse
# importamos modelos que se utilizan para las consultas
from .models import Post, User

def mostrarPosts(request):
    # select * from Post
    posts = Post.objects.all()
    posts_sep = ""
    for post in posts:
        posts_sep += f" ID: {post.id} --> {post.titulo}  <br>"

    return HttpResponse(posts_sep)

def mostrarUsuarios(request):
    # select * from User 
    # usuarios = User.objects.all()
    # return HttpResponse(usuarios)
    # Order_by(anombre_campo)
    usuarios = User.objects.all().order_by("id")
    usuarios_sep = ""
    for usuario in usuarios:
        usuarios_sep += f" ID: {usuario.id} --> {usuario.username}  <br>"

    return HttpResponse(usuarios_sep)


def filtrarPostID(request):
    # select * from Post where id=2
    post = Post.objects.get(id=2)
    return HttpResponse(post)


def eliminarPost(request):
    # select * from Post where id=1
    post = Post.objects.get(id=1)
    post.delete()

    return HttpResponse("Post eliminado")


def agregarPost(request):

    creador = User.objects.get(id=2)

    post = Post(autor=creador, titulo="Saludo", contenido="Hola mundo estoy creando un nuevo post desde la vista")
    post.save()

    return HttpResponse("Post creado")

def agregarPostVarios(request):
    # inster into Post(campos) 
    # values(valores), (valores),(valores)
    creador = User.objects.get(id=1)
    creador2 = User.objects.get(id=2)

    post1 = Post(autor=creador, titulo="Inflación", contenido="Mañana saldrá el dato de inflación del Mes de Junio")
    post2 = Post(autor=creador2, titulo="Final", contenido="El domingo se jugará la final del mundial de clubes CHE VS PSG")
    post3 = Post(autor=creador, titulo="Informatorio", contenido="Curso de informatio estamos en Django")
    
    Post.objects.bulk_create([post1,post2,post3])

    return HttpResponse("Posts creado")


def mostrarPostMenorId(request):
    #  __lt
    posts = Post.objects.filter(id__lte=4).order_by("fecha_creacion")
    posts_sep = ""
    for post in posts:
        posts_sep += f" ID: {post.id} --> {post.titulo}<br> {post.contenido}<br>{post.fecha_creacion}  <br><br><br>"

    return HttpResponse(posts_sep)
    

def mostrarPostMayorId(request):
    #  __lt
    posts = Post.objects.filter(id__gte=5).order_by("fecha_creacion")
    posts_sep = ""
    for post in posts:
        posts_sep += f" ID: {post.id} --> {post.titulo}<br> {post.contenido}<br>{post.fecha_creacion}  <br><br><br>"

    return HttpResponse(posts_sep)

def mostrarPostContains(request):
    #  __lt
    posts = Post.objects.filter(titulo__contains="Infl").order_by("fecha_creacion")
    posts_sep = ""
    for post in posts:
        posts_sep += f" ID: {post.id} --> {post.titulo}<br> {post.contenido}<br>{post.fecha_creacion}  <br><br><br>"

    return HttpResponse(posts_sep)