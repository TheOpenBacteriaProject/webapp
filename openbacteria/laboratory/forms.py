from django import forms



class crear_experimento_en_web(forms.Form):
    nombre = forms.CharField()
    bacteria = forms.CharField()
    temperatura = forms.DecimalField(max_digits=4,decimal_places=2)
    acidez = forms.DecimalField(max_digits=4,decimal_places=2)
    humedad = forms.DecimalField(max_digits=4,decimal_places=2)
    oxigeno = forms.DecimalField(max_digits=4,decimal_places=2)
    descripcion = forms.CharField()
