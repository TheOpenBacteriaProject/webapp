from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Bacterium, Experiment
from laboratory.fkpp2D_web import FKPP
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import crear_experimento_en_web
# Create your views here.

#Funciones de registro y login
def mostrar_index(request):
    return render(request, 'laboratory/index.html')

#Ni idea de que devuelve esto, pero tecnicamente el usuario
def get_queryset_actual_user(self):
    return Userproject.objects.filter(user=self.request.user)


def crear_experimento(name,user,slug,bacteria,temperature,acidity,humidity,oxigen,description):
    #Obtengo los datos para crear un experimento
    nombre = name
    slug = name
    bacteria =  bacteria
    temperatura = temperature
    acidez = acidity
    humedad = humidity
    oxigeno = oxigen
    descripcion = description

    experimento = Experiment(
        name = nombre,
        usuario = user,
        slug = slug,
        bacterium = bacteria,
        experiment_oxygen = oxigen,
        experiment_acidity = acidez,
        experiment_humidity = humedad,
        experiment_temperature = temperatura,
        description = descripcion
    )

    experimento.save()

#Para seguir aqui tengo que ver la forma de obtener datos de la pagian web
def generar_experimento(request):
    #Utiliza un experimento ya creado. Genera el experimento
    user=self.request.user
    nombre_experimento = AQUIFALTAOBTENERELEXPERIMENTO.name
    tiempo =51
    velocidad = 41
    #Por ahora alamacenamos las fotos en static
    FKPP(0,tiempo,velocidad,user,nombre_experimento)
    #Ahora tengo que cargar el proyecto en el html. habra que hacerlo con el contexto
    context = {}
    return render(request,'laboratorio.html'.context)

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
def mostrar_registro(request):
    return render(request,'registrar.html')

def register_user(request):
    form = UserCreationForm(request.POST)
    output = ''
    context = ''
    if form.is_valid():
        print('Hola paco')
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
    else:
        output = "fail_to_log.html"
        context = {'frase_de_error' : "registro ha fallado"}
    return render(request,output,context)

def crear_laboratorio(request):
    if request.method == 'POST':
        form = crear_experimento_en_web(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            #Llamo a la funcion para crear el experimento
            crear_experimento(
                name =          nombre,
                user =          User.objects.get(username='Enrique'),
                slug =          form.cleaned_data['nombre'],
                bacteria=       Bacterium.objects.get(name=form.cleaned_data['bacteria']),
                temperature =   form.cleaned_data['temperatura'],
                acidity =       form.cleaned_data['acidez'],
                humidity =      form.cleaned_data['humedad'],
                oxigen =        form.cleaned_data['oxigeno'],
                description =   form.cleaned_data['descripcion']
            )

            context = {
            'cargar_proyecto'   : "TRUE",
            'frase'             : "Experimento",
            'Temperatura'       : form.cleaned_data['temperatura'],
            'Humedad'           : form.cleaned_data['acidez'],
            'Oxigeno'           : form.cleaned_data['oxigeno'],
            'Acidez'            : form.cleaned_data['acidez'],
            'form'              : form
            }
    else:

        form = crear_experimento_en_web()

        context = {
        'frase'   : "Experimento",
        'form'    : form
        }
    return render(request,'laboratorio.html',context)
