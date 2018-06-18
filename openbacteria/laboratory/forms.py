from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class crear_experimento_en_web(forms.Form):
    BACTERIAS = {
        ('Bacteria1','Lactobacillus casei'),
        ('Levadura1','Saccharomyces cerevisiae')
    }
    nombre = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Nombre del experiemnto'}))
    bacteria = forms.ChoiceField(choices=BACTERIAS,label='')
    temperatura = forms.DecimalField(max_digits=4,decimal_places=2,label='',widget=forms.TextInput(attrs={'placeholder': 'Temperatura(0-100)'}))
    acidez = forms.DecimalField(max_digits=4,decimal_places=2,label='',widget=forms.TextInput(attrs={'placeholder': 'Acidez(0-14)'}))
    humedad = forms.DecimalField(max_digits=4,decimal_places=2,label='',widget=forms.TextInput(attrs={'placeholder': 'Humedad(0-100)'}))
    oxigeno = forms.DecimalField(max_digits=4,decimal_places=2,label='',widget=forms.TextInput(attrs={'placeholder': 'Oxigeno(0-100)'}))
    descripcion = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Descripcion'}))
