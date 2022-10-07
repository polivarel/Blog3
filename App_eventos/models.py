from django.db import models
from ckeditor.fields import RichTextField


class Evento_db(models.Model):
    titulo     = models.CharField(max_length=50,null=True)
    subtitulo  = models.CharField(max_length=100,null=True)
    cuerpo     = RichTextField(verbose_name="Contenido")
    autor      = models.CharField(max_length=100,null=True)
    fecha      = models.DateField()
    imagen     = models.ImageField(upload_to='', default=None)
    
    def __str__(self):
	    return self.titulo

