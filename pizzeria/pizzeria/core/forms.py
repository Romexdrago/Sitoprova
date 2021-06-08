from django import forms
from django.contrib.auth import models
from django.forms import fields, widgets
from .models import RecensioneModel

class RecensioneModelForm(forms.ModelForm):
    class Meta:
        model = RecensioneModel
        fields = ["contenuto","pizza_ordinata"]
        widgets = {
            "contenuto":forms.Textarea(attrs={"placeholder":"Inserisci la tua recensione","rows":"3"}),
            "pizza_ordinata": forms.TextInput(attrs={"placeholder": "Inserisci la tua pizza"})
        }
