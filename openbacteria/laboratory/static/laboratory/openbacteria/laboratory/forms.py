from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class crear_experimento_en_web(forms.Form):
    BACTERIAS = (
    ('ANAEROBIC','anaerobic'),
    ('AEROBIC','aerobic') )

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'ajustar_input'}))
    bacteria = forms.ChoiceField(choices=BACTERIAS,widget=forms.TextInput(attrs={'class': 'ajustar_input'}))
    temperatura = forms.DecimalField(max_digits=4,decimal_places=2,widget=forms.TextInput(attrs={'class': 'ajustar_input'}))
    acidez = forms.DecimalField(max_digits=4,decimal_places=2,widget=forms.TextInput(attrs={'class': 'ajustar_input'}))
    humedad = forms.DecimalField(max_digits=4,decimal_places=2,widget=forms.TextInput(attrs={'class': 'ajustar_input'}))
    oxigeno = forms.DecimalField(max_digits=4,decimal_places=2,widget=forms.TextInput(attrs={'class': 'ajustar_input'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'ajustar_input'}))


class registrar_usuario_modificado(UserCreationForm):

    def save(self,commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)

        if commit:
            user.save()

        return user
