from django.db import models

#Experiment es una entidad debil de bacterium
#User tiene una relacion muchos a muchos con Experiment


class Bacterium(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    #Clasifico las baterias por el tipo de respiracion que tienen. No es realmente importante, pero es un detalle.
    BACTERIUM_TYPE = (
    (ANAEROBIC,'anaerobic'),
    (AEROBIC,'aerobic')
    )
    baterium_type = models.CharField(max_length = 12, choices=BACTERIUM_TYPE)
    ideal_temperature = models.DecimalField(max_digits=3,decimal_places=2)
    ideal_humidity = models.DecimalField(max_digits=3,decimal_places=1)
    ideal_acidity = models.DecimalField(max_digits=2,decimal_places=2)
    ideal_oxygen = models.DecimalField(max_digits=3,decimal_places=1)
    description = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Experiment(models.Model):
    name = CharField(max_length = 100, unique=True)
    slug = SlugField(max_length=30,help_text='A label for URL config') #Esto es para configurar las URLs y que se vean guays.
    bacterium = models.ForeignKey(Bacterium,on_delete=models.CASCADE)
    experiment_temperature = models.DecimalField(max_digits=3,decimal_places=2)
    experiment_humidity = models.DecimalField(max_digits=3,decimal_places=1)
    experiment_acidity = models.DecimalField(max_digits=2,decimal_places=2)
    experiment_oxygen = models.DecimalField(max_digits=3,decimal_places=1)
    description = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        unique_together = ('bacterium','name') #Representa la relacion de entidad debil entre Experiment y Bacterium.

class User(models.Model):
    nickname = CharField(max_length = 25, unique=True)
    e-mail = models.EmailField()
    password = models.CharField(max_length = 50) #Habra que encriptarla o lo hace djgango?
    slug = SlugField(max_length=30,unique=True,help_text='A label for URL config')
    mad_experiments = models.ManyToManyField(Experiment)
    def __str__(self):
        return self.nickname
    class Meta:
        ordering = ['nickname']
