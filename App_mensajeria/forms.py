from logging import PlaceHolder
from multiprocessing.sharedctypes import Value
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from typing import Any, Dict, Iterable, List, Optional, Type, TypeVar, Union
from unittest.util import _MAX_LENGTH

import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import ValidationError
from django.db import models
#from django.forms.fields import _ClassLevelWidgetT
from django.forms.widgets import Widget
from django.http.request import HttpRequest





UserModel: Type[AbstractBaseUser]
_User = TypeVar("_User", bound=AbstractBaseUser)


    
#@login_required
class form_verMensajes(forms.ModelForm):
    first_name = forms.CharField( label='Nombre'   ,max_length=30, required=False, widget=forms.TextInput(attrs= {'title':'Escriba su nombre.'}))
    last_name  = forms.CharField( label='Apellido' ,max_length=30, required=False, widget=forms.TextInput(attrs= {'title':'Escriba su apellido'}))   
    username   = forms.CharField( label='Usuario'  ,max_length=30, required=True , widget=forms.TextInput(attrs= {'title':'Requerido. 30 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.'}))  
    email      = forms.EmailField(label='Correo'   ,max_length=254,required=True , widget=forms.EmailInput(attrs={'title':'Requerido. Ingrese una dirección de correo electrónico válida.'}))
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email' ]




class Form_mensajeA(forms.ModelForm):
    mensaje = forms.CharField(label='')
    class Meta:
        model = User
        fields = ['mensaje']
