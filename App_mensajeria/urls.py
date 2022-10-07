from django.urls import path

from App_mensajeria.views import *



urlpatterns = [
    path("verContactos/"           , verContactos , name="verContactos"),
    path("mensajeA/<id>/<nick>"    , mensajeA     , name="Form_mensajeA"   ),
    path("mensajes/<id1>/<id2>"    , mensajes     , name="Form_mensajes"   ),
    path("mensajes_old/<id1>/<id2>/<nick>", mensajes_old , name="mensajes_old"    ),
]