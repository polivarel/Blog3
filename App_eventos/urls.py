"""Blog3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from App_administrador.views import *
from App_eventos.views import *
from App_mensajeria.views import *
from App_principal.views import *
from App_usuarios.views import *


urlpatterns = [
    path("eventoFormulario/", evento, name="evento_Formulario"),
    path("pages/", leerEventos, name="leerEventos"),
    path("eliminarEvento/<id>", eliminarEvento, name="eliminarEvento"),
    path("editarEvento/<id>", editarEvento, name="editarEvento"),
    path("pages/<id>", leerMas, name="leerMas"),    
    
]
