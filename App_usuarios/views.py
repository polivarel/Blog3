from App_usuarios.forms import *
from App_eventos.models import *
from App_usuarios.models import *
from App_usuarios.views import *


from email.mime import image
from pydoc import visiblename
from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import *
from django.template import RequestContext , loader
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy    
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required




from django.shortcuts import render


def crear_usuario(request):
    if request.method == 'POST':
        form = form_crear_usuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            return render(request, 'index.html', {'mensaje':username})
        else:
            return render(request, "usuarios/crear.html", {"formulario":form})    
    else:
        form = form_crear_usuario()
        return render(request, 'usuarios/crear.html', {'formulario': form, "avatar":obtenerAvatar(request)})

def form_ingresar_usuario(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'usuarios/ingresar.html', {'mensaje':"ok"})
            else:
                return render(request, "usuarios/ingresar.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "usuarios/ingresar.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "usuarios/ingresar.html", {"formulario":form, "avatar":obtenerAvatar(request)})

@staff_member_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    imagen=Avatar.objects.all()
    #if len(lista) != 0:
    #    imagen = lista[0].imagen.url
    #else:
    #    imagen = "/media/avatares/_perfil.jpg"
    return render(request, "usuarios/listar.html", {"usuarios":usuarios, "avatar":obtenerAvatar(request)})

@login_required
def editar_usuarios(request,id):
    usuario = User.objects.get(id=id)
    if request.method == 'POST':
        form = form_editar_usuarios(request.POST,instance=usuario)
        if form.is_valid():
            usuario.username   = form.cleaned_data.get('username')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name  = form.cleaned_data.get('last_name')
            usuario.email      = form.cleaned_data.get('email')
            usuario.save()
            if usuario.is_superuser:
                return redirect('/App_usuarios/listar_usuarios/')
            else:
                return redirect('/App_usuarios/accounts/profiles')
        else:
            return render(request, "usuarios/editar.html", {"formulario":form, "usuario":usuario, "mensaje":"FORMULARIO INVALIDO"})
    else:
        form = form_editar_usuarios(instance=usuario)
        return render(request, 'usuarios/editar.html', {'formulario': form, "usuario":usuario, "avatar":obtenerAvatar(request)})

@staff_member_required
def eliminar_usuario(request,id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return render(request, 'usuarios/listar.html', {"usuario":usuario,"mensaje":"Usuario eliminado correctamente!"})

@login_required
def ver_perfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
        return render (request, "usuarios/perfil.html", {"avatar":obtenerAvatar(request), "user":user})
        

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo= Avatar.objects.filter(user=request.user)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()
            
            avatar=Avatar(user = request.user, imagen = formulario.cleaned_data['imagen'])
            avatar.save()
            return render (request, "usuarios/perfil.html", {"usuario":request.user ,"avatar":obtenerAvatar(request), "mensaje":"Avatar agregado exitosamente!!",
            "imagen":avatar.imagen.url})
        else:
            return render (request, "usuarios/agregarAvatar.html", {"formulario":formulario, "mensaje":"FORMULARIO INVALIDO!!"})
    else:
        formulario=AvatarForm()
        return render (request, "usuarios/agregarAvatar.html" , {"formulario":formulario , "usuario":request.user, "avatar":obtenerAvatar(request)})

@login_required
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista) != 0:
        imagen = lista[0].imagen.url
    else:
        imagen = "/media/avatares/_perfil.jpg"
    return imagen
                            