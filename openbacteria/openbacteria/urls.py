"""openbacteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#App imports
from laboratory.views import *


urlpatterns = [
    path(r'', mostrar_index),
    path(r'logear_usuario_en_index/',login_user),
    path(r'ir_a_registro/',mostrar_registro),
    path(r'registrar_usuario/',register_user),
    path(r'admin/', admin.site.urls),
    path(r'laboratorio/', crear_laboratorio),
]
