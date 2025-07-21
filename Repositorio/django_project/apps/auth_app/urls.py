
from django.urls import path
from .views import exit, RegisterView

urlpatterns = [
    path('logout/', exit, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    
]