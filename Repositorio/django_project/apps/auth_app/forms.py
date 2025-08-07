
# username y password
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(required=True, 
                             widget=forms.EmailInput(attrs={
                                 'class':'form-control', 'placeholder': 'name@example.com' }
                                 ))

    username = forms.CharField(required=True, label="Nombre de usuario", max_length=50, widget=forms.TextInput(attrs={
                                 'class':'form-control', 'placeholder': 'Ingrese su nombre de usuario'}
                                 ))

    first_name = forms.CharField(required=True, label="Nombre", max_length=50, widget=forms.TextInput(attrs={
                                 'class':'form-control', 'placeholder': 'Ingrese su nombre'}
                                 ))
    
    last_name = forms.CharField(required=True, label="Apellido", max_length=50, widget=forms.TextInput(attrs={
                                 'class':'form-control', 'placeholder': 'Ingrese su apellido'}
                                 ))
    
    password1 = forms.CharField(required=True, label="Contraseña", widget=forms.PasswordInput(attrs={
                                 'class':'form-control', 'placeholder': 'Contraseña'}
                                 ))

    password2 = forms.CharField(required=True, label="Confirmar contraseña", max_length=50, widget=forms.PasswordInput(attrs={
                                 'class':'form-control', 'placeholder': 'Repetir contraseña'}
                                 ))


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")



    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user