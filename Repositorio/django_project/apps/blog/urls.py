
from django.urls import path
from . import views

urlpatterns = [
    path('mostrarPosts/', views.mostrarPosts),
    path('mostrarUsuarios/', views.mostrarUsuarios),
    path('filtrarPostID/', views.filtrarPostID),
    path('eliminarPost/', views.eliminarPost),
    path('cargarPost/', views.agregarPost),
    path('cargarPostVarios/', views.agregarPostVarios),
    path('menorID/', views.mostrarPostMenorId),
    path('mayorID/', views.mostrarPostMayorId),
    path('contains/', views.mostrarPostContains),
]