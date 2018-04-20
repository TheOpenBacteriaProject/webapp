from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class crear_experimento_en_web(forms.Form):
    nombre = forms.CharField()
    bacteria = forms.CharField()
    temperatura = forms.DecimalField(max_digits=4,decimal_places=2)
    acidez = forms.DecimalField(max_digits=4,decimal_places=2)
    humedad = forms.DecimalField(max_digits=4,decimal_places=2)
    oxigeno = forms.DecimalField(max_digits=4,decimal_places=2)
    descripcion = forms.CharField()

class registrar_usuario_modificado(UserCreationForm):

    def save(self,commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)

        if commit:
            user.save()

        return user
