from contextlib import AbstractAsyncContextManager
from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Evento_db(models.Model):
    propietario= models.CharField(max_length=100,null=True)
    titulo     = models.CharField(max_length=50,null=True)
    subtitulo  = models.CharField(max_length=100,null=True)
    cuerpo     = RichTextField(verbose_name="Contenido")
    #cuerpo     = models.CharField(max_length=1000,null=True)
    autor      = models.CharField(max_length=100,null=True)
    fecha      = models.DateField()
    imagen     = models.ImageField(upload_to='media/', default=None)
    
    def __str__(self):
	    return self.titulo

