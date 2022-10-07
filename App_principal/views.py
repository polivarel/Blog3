from django.shortcuts import render
from django.shortcuts import render, redirect
from App_eventos.models import *

def index(request):
    return render (request, "index.html")
    
def about(request):
    return render(request, "about.html")    