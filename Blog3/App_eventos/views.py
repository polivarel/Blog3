from App_eventos.models import *
from django import forms
from App_eventos.forms import *


from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from typing import Any, Dict, Iterable, List, Optional, Type, TypeVar, Union
from unittest.util import _MAX_LENGTH

from django.contrib.auth.decorators import login_required
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import ValidationError
from django.db import models
#from django.forms.fields import _ClassLevelWidgetT
from django.forms.widgets import Widget
from django.http.request import HttpRequest
from .models import Evento_db 
import datetime
from django.utils import timezone

from django.shortcuts import render

# Create your views here.
def evento(request):
    if request.method=="POST":
        form=EventoForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            propietario=informacion['propietario']
            titulo=informacion['titulo']
            subtitulo=informacion['subtitulo']
            cuerpo=informacion['cuerpo']
            autor=informacion['autor']
            fecha=informacion['fecha']
            imagen=informacion['imagen']
            evento=Evento_db(propietario=propietario, titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            evento.save()
            return render(request, "leerEventos.html",{"mensaje":"Evento creado correctamente"})
        else:
            return render(request, "eventoFormulario.html",{"mensaje":"Formulario invalido"})
    else:
        form=EventoForm()
        return render(request, "eventoFormulario.html", {"formulario_evento":form})





def leerEventos(request):
    eventos=Evento_db.objects.all()
    return render(request, "leerEventos.html", {"eventos": eventos})

def eliminarEvento(request, id):
    evento=Evento_db.objects.get(id=id)
    evento.delete()
    eventos=Evento_db.objects.all()
    return render(request, "leerEventos.html", {"eventos": eventos})

def editarEvento(request, id):
    evento=Evento_db.objects.get(id=id)
    if request.method=="POST":
        form=EventoForm(request.POST, request.FILE)
        if form.is_valid():
            info=form.cleaned_data
            evento.propietario=info["propietario"]
            evento.titulo=info["titulo"]
            evento.subtitulo=info["subtitulo"]
            evento.cuerpo=info["cuerpo"]
            evento.autor=info["autor"]
            evento.fecha=info["fecha"]
            evento.imagen=info["imagen"]
            evento.save()
            eventos=Evento_db.objects.all()
            return render(request, "leerEventos.html", {"eventos":eventos})
        else:
            form=EventoForm(initial={"propietario":evento.propietario, "titulo":evento.titulo, "subtitulo":evento.subtitulo, "cuerpo":evento.cuerpo, "autor":evento.autor, "fecha":evento.fecha, "imagen":evento.imagen})
            return render(request, "editarEvento.html", {"formulario":form, "evento":evento})
    else:
        form=EventoForm()
        return render(request, "eventoFormulario.html", {"formulario":form})


def leerEventos(request):
    eventos=Evento_db.objects.all()
    return render(request, "leerEventos.html", {"eventos": eventos})

def leerMas(request, id):
    evento=Evento_db.objects.get(id=id)
    return render(request, "leerMas.html", {"evento":evento})