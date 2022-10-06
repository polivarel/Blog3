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
from django.db.models import Q
from django.http import JsonResponse


def verContactos(request):
    usuarios = User.objects.all()
    return render(request, "mensajes/contactos.html", {"usuarios":usuarios})



def mensajeA(request,id,nick):
    if request.method == 'POST':
        form = Form_mensajeA(request.POST)
        if form.is_valid():
            mensaje = form.cleaned_data.get('mensaje')
            #password = form.cleaned_data.get('password1')
            form=mensajes_db(mensaje=mensaje, receptor=id, emisor=request.user.id)
            form.save()
            #return render(request, 'mensajes/mensajeA.html', {'id':id, 'nick':nick})
            return redirect('Form_mensajeA', id=id, nick=nick )
        else:
            return render(request, "mensajes/mensajeA.html", {"formulario_casilla":form})    
    else:
        form = Form_mensajeA()
        return render(request, 'mensajes/mensajeA.html', {'id':id,'nick':nick,'formulario_mensajeA': form})




def mensajes(request,id1,id2):
    mensajes = mensajes_db.objects.filter(
        Q(emisor=id1, receptor=id2) | Q(emisor=id2, receptor=id1)
    ).order_by('-id')
    return render(request, "mensajes/mensajes.html", {"mensajes":mensajes})


def mensajes_old(request,id1,id2,nick):
    mensajes = mensajes_db.objects.filter(
        Q(emisor=id1, receptor=id2) | Q(emisor=id2, receptor=id1)
    ).order_by('id')
    return render(request, "mensajes/mensajesAntiguos.html", {"mensajes":mensajes,"nick":nick,"id1":id1})