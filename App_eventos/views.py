from App_eventos.models import *
from django import forms
from App_eventos.forms import *


from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from typing import Any, Dict, Iterable, List, Optional, Type, TypeVar, Union
from unittest.util import _MAX_LENGTH

from django.contrib.admin.views.decorators import staff_member_required
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

from django.shortcuts import render, redirect


@login_required
def evento(request):
    if request.method=="POST":
        form=EventoForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion['titulo']
            subtitulo=informacion['subtitulo']
            cuerpo=informacion['cuerpo']
            autor=informacion['autor']
            fecha=informacion['fecha']
            imagen=informacion['imagen']
            evento=Evento_db( titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            evento.save()
            return redirect('/App_principal/pages/')
        else:
            return render(request, "eventoFormulario.html",{"mensaje":"Formulario invalido"})
    else:
        form=EventoForm()
        return render(request, "eventoFormulario.html", {"formulario_evento":form})

@login_required
def leerEventos(request):
    eventos=Evento_db.objects.all()
    return render(request, "leerEventos.html", {"eventos": eventos})

@staff_member_required
def eliminarEvento(request, id):
    evento=Evento_db.objects.get(id=id)
    evento.delete()
    eventos=Evento_db.objects.all()
    return render(request, "leerEventos.html", {"eventos": eventos})

@staff_member_required
def editarEvento(request, id):
    evento=Evento_db.objects.get(id=id)
    if request.method=="POST":
        form=EditarEventoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            evento.titulo    =info["titulo"]
            evento.subtitulo =info["subtitulo"]
            evento.cuerpo    =info["cuerpo"]
            evento.fecha     =info["fecha"]
            evento.save()
            eventos=Evento_db.objects.all()
            return render(request, "leerEventos.html", {"eventos":eventos})
    else:
        form=EditarEventoForm(initial={ "titulo":evento.titulo, "subtitulo":evento.subtitulo, "cuerpo":evento.cuerpo, "fecha":evento.fecha, "imagen":evento.imagen})
        return render(request, "editarEvento.html", {"formulario":form, "evento":evento})
    





@staff_member_required
def editarFotoEvento(request, id):
    evento=Evento_db.objects.get(id=id)
    if request.method=="POST":
        form=Foto_EventoForm(request.POST,request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            evento.imagen =informacion["imagen"]
            evento.save()
            return redirect('/App_eventos/editarEvento/'+id)
    else:
        form=Foto_EventoForm()
        return render(request, "Evento_editar_foto.html", {"form_Editar_Imagen_Evento":form, "evento":evento})





def leerMas(request, id):
    evento=Evento_db.objects.get(id=id)
    return render(request, "leerMas.html", {"evento":evento})