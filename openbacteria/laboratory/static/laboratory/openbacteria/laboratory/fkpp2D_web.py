#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CODIGO PARA EJECUCION DENTRO DEL BACKEND DE LA WEB
Presentamos  la funcion con el algoritmo mediante el cual podemos generar la simulacion en 3d
de la ecuacion FKPP. El proceso seguido es el que se puede encontrar en la
documentacion del proyecto.
Este codigo nos sirve para interactuar con la web y la base de datos de forma óptima, dejando
para la inspección los otros códigos. Todos los que tenga esto como fin vendrán marcados
con el identificativo: WEB
@author: TheOpenBacteriaProject
"""
#Importamos distintas librerías utiles para el desarrollo del codigo en todos los códigos
#para poder usarlos en el mismo ide simultáneamente y poder desplazar trozos de unos a
#otros sin preocuparnos por la compatibillidad. El fin de estos códigos es científico pero
#también educativo, por tanto, creemos que este puede ser un bun enfoque.

from time import time
import numpy
import math
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show,savefig
import matplotlib.colors as mcolors
import sys
import matplotlib.pyplot as plt
from .models import Image
#Describimos el algoritmo prinicipal.
#La funcion recibe tres parametros
#1º u  => Matriz de datos
#2º nt => Tiempo del experimento
#3º v  => Velocidad del experimento
def make_colormap(seq):
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)

#Argumentos
#1º matriz de datos
#2º Tiempo
#3º Velocidad
#4º Precision. Tomar una imagen cada x tiempo
#5º Usuario. Nombre del usuario
#6º Nombre del experimento
def FKPP(u,nt,v,precision,usuario,nombre_experimento):
    nx = 50
    ny = 50
    vel= v
    nu = .02
    dx = 10.0 / (nx - 1) #discretizaciones
    dy = 10.0 / (ny - 1)
    sigma = .01
    dt = sigma * dx * dy / nu

    x = numpy.linspace(-5, 5, nx)
    y = numpy.linspace(-5, 5, ny)
    if u == 0:
        u = numpy.ones((ny, nx)) 
        u[int(3.5/dy):int(4.0/dy+1),int(3.5/dx):int(4.0/dx+1)] = 2
        u[int(8./dy):int(8.5/dy+1),int(6.0/dx):int(6.5/dx+1)] = 2
        for i in range(0,nx):
            for j in range(0,ny):
                if u[i][j]!=2:
                    u[i][j]=0 ##Nos aseguramos de que no haya bacterias en ningun otro punto
    #Ciclo para la evolucion descrita en la documentación.
    for n in range(nt + 1):
        un = u.copy()
        u[1:-1, 1:-1] = (un[1:-1,1:-1] + vel*nu * dt / dx**2 *(un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +vel*nu * dt / dy**2 * (un[2:,1: -1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])+dt*un[1:-1,1:-1]-dt*un[1:-1,1:-1]*un[1:-1,1:-1]/2)
        u[0, :] = 0
        u[-1, :] = 0
        u[:, 0] = 0
        u[:, -1] = 0

        #Este ciclo nos permite acotar el crecimiento de la bacteria a un circulo
        #Ante la posibilidad de saltos por la discretizacion numérica exite aunque
        #seria poco represetnativa
        ##Abrimos la puerta para una futura mejora del codigo, pasando a coordenadas
        ##polares, pero el limitado tiempo nos lo ha impedido.

        for angle in range(0, 360, 5):
            x = 24 * math.sin(math.radians(angle)) + int(round((nx/2.0)-1))
            y = 24 * math.cos(math.radians(angle)) + int(round((nx/2.0)-1))
            for i in range(0,nx):
                for j in range(0,nx):
                    if i==int(round(x)) and j==int(round(y)):
                        u[i][j]=0

        if n%precision == 0:
             guardar_imagen(u,n,usuario,nombre_experimento)
    #Este último ciclo (que debe estar fuera del principal para que la aproximacion
    #no afecte al desarrollo normal de la evolucion temporal), nos sirve para
    #aproximar la sensibilidad de los resultados, eliminando los elementos que estén
    #por debajo de un rango para paliar la difusión infinita generada por el uso de la
    #ecuacion de difusión clásica.
    #Incluir modelos de flujo limitado es otra de los futuros avances planeados
    for i in range(0,nx):
        for j in range(0,nx):
            if u[i][j]<=0.4:
                u[i][j]=0


    return u


def guardar_imagen(u,contador,usuario, nombre_experimento):
        c = mcolors.ColorConverter().to_rgb
        rvb = make_colormap([c('c'), c('orange'), c('darkorange')])
        im = imshow(u,cmap=rvb) # dibujamos la función
        # Añadimos las lineas de contorno y las etiquetas a cada una.
        cset = contour(u,arange(0.7,2,0.3),linewidths=1,cmap=cm.binary)
        clabel(cset,inline=False,fmt='%1.1f',fontsize=10)
        if contador == 0:
                colorbar(im) # Añadimos la barra de color a la derecha
        title('concetracion bacterias')
        #La ruta sera: static/laboratory/user/experiment/image+contador
        name = "/home/espectro/Escritorio/openbacteria/laboratory/static/laboratory/"+ usuario + "/" + nombre_experimento +"-"+ "imagen" +"-"+ str(contador)
        savefig(name)
        imagen = Image()
        plt.clf()
        plt.cla()
        plt.close()
