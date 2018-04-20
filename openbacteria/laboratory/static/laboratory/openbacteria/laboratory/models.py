from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#Experiment es una entidad debil de bacterium
#User tiene una relacion muchos a muchos con Experiment


class Bacterium(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    #Clasifico las baterias por el tipo de respiracion que tienen. No es realmente importante, pero es un detalle.
    BACTERIUM_TYPE = (
    ('ANAEROBIC','anaerobic'),
    ('AEROBIC','aerobic')
    )
    bacterium_type = models.CharField(max_length = 12, choices=BACTERIUM_TYPE)
    ideal_temperature = models.DecimalField(max_digits=4,decimal_places=2)
    ideal_humidity = models.DecimalField(max_digits=4,decimal_places=2)
    ideal_acidity = models.DecimalField(max_digits=4,decimal_places=2)
    ideal_oxygen = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Experiment(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Usa auth de django
    slug = models.SlugField(max_length=30,help_text='A label for URL config')
    bacterium = models.ForeignKey(Bacterium,on_delete=models.CASCADE)
    experiment_temperature = models.DecimalField(max_digits=4,decimal_places=2)
    experiment_humidity = models.DecimalField(max_digits=4,decimal_places=2)
    experiment_acidity = models.DecimalField(max_digits=4,decimal_places=2)
    experiment_oxygen = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        unique_together = ('bacterium','name','usuario') #Representa la relacion de entidad debil entre Experiment y Bacterium.

class Image(models.Model):
    theimage = models.ImageField(upload_to='img/',null = True)
    from_experiment = models.ForeignKey(Experiment,on_delete=models.CASCADE)
    def __str__(self):
        return self.theimage.url
