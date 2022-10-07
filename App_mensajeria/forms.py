from multiprocessing.sharedctypes import Value
from django import forms
from django.contrib.auth.models import User

from typing import Type, TypeVar, Union

from django.contrib.auth.base_user import AbstractBaseUser



UserModel: Type[AbstractBaseUser]
_User = TypeVar("_User", bound=AbstractBaseUser)


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
