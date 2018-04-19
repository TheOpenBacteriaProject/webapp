from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Bacterium, Experiment
from laboratory.fkpp2D_web import FKPP
# Create your views here.

#Funciones de registro y login
def mostrar_index(request):
    return render(request, 'laboratory/index.html')

#Aqui logeamos un usuario
def login_user(request):
    usuario = request.POST('usuario')
    password = request.POST('password')

    user = authenticate(request, username = usuario, password = password)

    #Si el usuario es correcto
    if user is not None:
        login(request,user) #Aqui tecnicamente ya tenemos el usuario logeado, solo tenemos que cargar el laboratorio con su base de datos
        crear_laboratorio(request)
    else:
        output = "fail_to_log.html"
        context = {'frase_de_error' : "Login fallido. usuario o contraseña incorrecto"}
    return render(request,output)

#Aqui registramos un nuevo usuario
def register_user(request):
    usuario = request.POST('usuario')
    password = request.POST('password')
    email = request.POST('email')

    #Deberiamos hacer un preprocesamiento de los campos, a no ser que lo haga django
    user = User.objects.create_user(username = usuario, email = email, password = password)

    #Si el usuario se ha creado correctamente
    if user is not None:
        output = "index.html"
    else:
        output = "fail_to_log.html"
        context = {'frase_de_error' : "La operacion de registro ha fallado horriblemente."}
    return render(request,output,context)

def crear_laboratorio(request):
    context = {
        'title' : "Open Bacteria",
        'frase' : "your petri dish",
        'frase2' : "experiment with your petri dish here"
    }
    return render(request,'laboratorio.html',context)
