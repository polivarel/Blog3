"""Blog3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.contrib.auth.views import LogoutView

from django.conf import settings #add this
from django.conf.urls.static import static #add this


from App_administrador.views import *
from App_eventos.views import *
from App_mensajeria.views import *
from App_principal.views import *
from App_usuarios.views import *


urlpatterns = [
    path("ingresar/", form_ingresar_usuario, name="form_ingresar_usuario"),
    path("form_crear_usuario/", crear_usuario, name="form_crear_usuario"),
    path('salir', LogoutView.as_view(next_page="ingresar/"), name='salir'),
    path("listar_usuarios/", listar_usuarios, name="listar_usuarios"),
    path("editar_usuarios/<int:id>", editar_usuarios, name="form_editar_usuarios"),
    path("listar_usuarios/", listar_usuarios, name="listar_usuarios"),
    path("eliminar_usuario/<int:id>", eliminar_usuario, name="form_eliminar_usuario"),
    path("ver_perfil/", ver_perfil, name="ver_perfil"), 
]
