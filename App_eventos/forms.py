from django import forms


from .models import Evento_db 
from django.utils import timezone
from ckeditor.fields import RichTextField



class EventoForm(forms.ModelForm):
    titulo     =forms.CharField(max_length=100)
    subtitulo  =forms.CharField()
    cuerpo     =RichTextField(verbose_name="Contenido")
    autor      =forms.CharField(max_length=100)
    fecha      =forms.DateField(widget=forms.SelectDateWidget, initial=timezone.now())
    imagen     =forms.ImageField()
    
    class Meta:
        model = Evento_db
        fields = ('titulo', 'subtitulo', 'cuerpo', 'autor','fecha','imagen')


class EditarEventoForm(forms.ModelForm):
    titulo     =forms.CharField(max_length=100)
    subtitulo  =forms.CharField()
    cuerpo     =RichTextField(verbose_name="Contenido")
    fecha      =forms.DateField(widget=forms.SelectDateWidget, initial=timezone.now())
    class Meta:
        model = Evento_db
        fields = ('titulo', 'subtitulo', 'cuerpo', 'fecha')        



class Foto_EventoForm(forms.ModelForm):
    imagen=forms.ImageField()
    class Meta:
        model = Evento_db
        fields = ('imagen',)