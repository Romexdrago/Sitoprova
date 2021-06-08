from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegistrazioneForm(UserCreationForm):
    email=forms.CharField(max_length=35,widget=forms.EmailInput(attrs={"placholder":"Inserisci la tua mail"}))
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
