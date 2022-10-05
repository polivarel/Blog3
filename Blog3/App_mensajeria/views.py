from django.shortcuts import render

from pydoc import visiblename
from django.shortcuts import render, redirect
from django.http import HttpResponse

from random import *
from django.template import loader
from App_mensajeria.forms import *
from App_mensajeria.models import *

#from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy    

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate, get_user_model

from django.contrib.auth.decorators import login_required



def verMensajes(request):
    usuarios = User.objects.all()
    #user = User.objects.get(username=request.user.username)
    return render(request, "mensajes/listar.html", {"usuarios":usuarios})

def mensajeA(request,id):
    if request.method == 'POST':
        form = Form_mensajeAa(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            return render(request, 'mensajes/casilla.html', {'mensaje':username})
        else:
            return render(request, "mensajes/casilla.html", {"formulario_casilla":form})    
    else:
        form = Form_mensajeAa()
        return render(request, 'mensajes/casilla.html', {'formulario_casilla': form})


    #usuarios = User.objects.all()
    #user = User.objects.get(username=request.user.username)
    #return render(request, "mensajes/casilla.html", {"usuarios":usuarios})