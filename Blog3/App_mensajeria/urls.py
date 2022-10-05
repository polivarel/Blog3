from django.contrib import admin
from django.urls import include, path

from django.contrib.auth.views import LogoutView
from App_mensajeria.views import *

#linea reservada para Pablo
#linea reservada para Pablo
#linea reservada para Pablo
#linea reservada para Pablo





urlpatterns = [
    
    path("mensajes/", verMensajes , name="verMensajes"),
    path("mensajeA/<int:id>", mensajeA , name="Form_mensajeA"),



]