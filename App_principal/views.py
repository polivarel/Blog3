from django.shortcuts import render
from django.shortcuts import render, redirect
from App_eventos.models import *
from App_usuarios.models import *
from App_usuarios.views import *

def index(request):
    return render (request, "index.html", {"avatar":obtenerAvatar(request)})
    
def about(request):
    return render(request, "about.html", {"avatar":obtenerAvatar(request)})    