from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Bacterium, Experiment, Image
from laboratory.fkpp2D_web import FKPP
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import crear_experimento_en_web, registrar_usuario_modificado
# Create your views here.

#Funciones de registro y login
def mostrar_index(request):
    #FKPP(0,200,1,10,"Bart","experimento-demo")
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
    if request.method == 'POST':
        form = registrar_usuario_modificado(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(r'')

    form = registrar_usuario_modificado()
    context = {'form' : form}

    return render(request,'registrar.html',context)

#Crea el laboratorio
def crear_laboratorio(request):
    if request.method == 'POST':
        form = crear_experimento_en_web(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            #Llamo a la funcion para crear el experimento
            form = crear_experimento_en_web()
            experimento = Experiment.objects.get(name="Enrique-django") #Obtengo el experimento
            imagenes = Image.objects.filter(from_experiment=experimento) #Obtengo las imagenes del experimento
            frase = "Experimento: Top secret experiment"
            usuario = "Usuario: Bart"

            context = {
            'form'          : form,
            'experimento'   : experimento,
            'imagenes'      : imagenes,
            'frase'         : frase,
            'usuario'          : usuario,

            }
            return render(request,'laboratorio.html',context)
        else:

            form = crear_experimento_en_web()
            experimento = Experiment.objects.get(name="Enrique-django") #Obtengo el experimento
            imagenes = Image.objects.filter(from_experiment=experimento) #Obtengo las imagenes del experimento
            frase = "Experimento: Top secret experiment"
            usuario = "Usuario: Bart"
            context = {
            'form'          : form,
            'experimento'   : experimento,
            'imagenes'      : imagenes,
            'frase'         : frase,
            'usuario'          : usuario,

            }

            return render(request,'laboratorio.html',context)

    else:

        form = crear_experimento_en_web()

        experimento = Experiment.objects.get(name="Enrique-django") #Obtengo el experimento
        imagenes = Image.objects.filter(from_experiment=experimento) #Obtengo las imagenes del experimento
        frase = "Top secret experiment"
        usuario = "Bart"
        context = {
        'form'          : form,
        'experimento'   : experimento,
        'imagenes'      : imagenes,
        'frase'         : frase,
        'usuario'       : usuario,

        }

        return render(request,'laboratorio.html',context)

#Crea el laboratorio demo
def crear_laboratorio_demo(request):

    form = crear_experimento_en_web()

    experimento = Experiment.objects.get(name="experimento-demo") #Obtengo el experimento
    imagenes = Image.objects.filter(from_experiment=experimento) #Obtengo las imagenes del experimento
    frase = "Experimento-nuevo"
    usuario = "Bart"
    context = {
        'form'          : form,
        'experimento'   : experimento,
        'imagenes'      : imagenes,
        'frase'         : frase,
        'usuario'       : usuario,

        }

    return render(request,'laboratorio.html',context)

#Metodo sin sentido ya. Dejarlo por ahora por si hace falta mirarlo pero borrarlo para el despliege
def laboratorio_basico(request):
    experimento = Experiment.objects.get(name="Enrique-django") #Obtengo el experimento
    imagenes = Image.objects.filter(from_experiment=experimento) #Obtengo las imagenes del experimento

    context = {
    'experimento'   : experimento,
    'imagenes'      : imagenes,
    'numero_imagenes' : numero_imagenes
    }
    return render(request,'basic_laboratory.html',context)
