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
    FKPP(0,100,1,10,"Enrique","Enrique-django")
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
    u = 0
    tiempo = 100
    velocidad = 1
    precision = 10
    usuario = "Enrique"
    proyecto = "Enrique-django"
    FKPP(u,tiempo,velocidad,precision,usuario,proyecto)

    for i in tiempo:
        if tiempo%i == 0:
            nombre_foto = usuario+"-"+proyecto+"-"+i
            imagen = Image(theimage="/static/laboratory/"+usuario+"/"+proyecto+"/"+nombre_foto)
            imagen.save()

    experimento = Experiment.objects.get(name=proyecto)
    #Ahora obtengo la querry con las imagenes del proyecto y las envio a la web
    imagenes = image.objects.filter(from_experiment=experimento)

    #Creo el contexto para enviarlo a la web
    context = {
    'experimento'   :   experimento,
    'imagenes'      :   imagenes,
    'titulo'        :   experimeno.name
    }

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

        experimento = Experiment.objects.get(name="Enrique-django") #Obtengo el experimento
        imagenes = Image.objects.filter(from_experiment=experimento) #Obtengo las imagenes del experimento

        context = {
        'frase'         : "Experimento",
        'form'          : form,
        'experimento'   : experimento,
        'imagenes'      : imagenes
        }
    return render(request,'laboratorio.html',context)

def laboratorio_basico(request):
    experimento = Experiment.objects.get(name="Enrique-django") #Obtengo el experimento
    imagenes = Image.objects.filter(from_experiment=experimento) #Obtengo las imagenes del experimento
    numero_imagenes = imagenes.count()
    context = {
    'experimento'   : experimento,
    'frase'         : "Hola caracola",
    'imagenes'      : imagenes,
    'numero_imagenes' : numero_imagenes
    }
    return render(request,'basic_laboratory.html',context)
