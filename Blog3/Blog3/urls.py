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
from django.urls import path, include

from App_administrador.views import *
from App_eventos.views import *
from App_mensajeria.views import *
from App_principal.views import *
from App_usuarios.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  

    path('App_administrador/', include('App_administrador.urls')),
    path('App_eventos/'      , include('App_eventos.urls')),
    path('App_mensajeria/'   , include('App_mensajeria.urls')),
    path('App_principal/'    , include('App_principal.urls')),
    path('App_usuarios/'     , include('App_usuarios.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

