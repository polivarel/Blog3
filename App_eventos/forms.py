from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from typing import Any, Dict, Iterable, List, Optional, Type, TypeVar, Union
from unittest.util import _MAX_LENGTH

from datetime import datetime

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
from ckeditor.fields import RichTextField



class EventoForm(forms.ModelForm):
    propietario=forms.CharField(max_length=100)
    titulo     =forms.CharField(max_length=100)
    subtitulo  =forms.CharField()
    cuerpo     =RichTextField(verbose_name="Contenido")
    autor      =forms.CharField(max_length=100)
    fecha      =forms.DateField(widget=forms.SelectDateWidget, initial=timezone.now())
    imagen     =forms.ImageField()
    
    class Meta:
        model = Evento_db
        fields = ('propietario', 'titulo', 'subtitulo', 'cuerpo', 'autor','fecha','imagen')