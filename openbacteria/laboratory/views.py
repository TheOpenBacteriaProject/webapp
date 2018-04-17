from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Bacterium

# Create your views here.


def mostrar_bacterias(request):
    lista_bacterias = Bacterium.objects.all()
    output = ''
    output += ', '.join([bacteria.name for bacteria in lista_bacterias])
    output += '\n'
    output += ', '.join([bacteria.description for bacteria in lista_bacterias])
    return HttpResponse(output)
