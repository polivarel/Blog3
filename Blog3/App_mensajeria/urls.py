from django.contrib import admin
from django.urls import include, path

from App_mensajeria.views import *



urlpatterns = [
    path("verContactos/"        , verContactos , name="verContactos"),
    path("mensajeA/<int:id>", mensajeA    , name="mensajeA"   ),
]