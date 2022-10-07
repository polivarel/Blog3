from django.db import models

class mensajes_db(models.Model):
    id       = models.AutoField(primary_key=True)
    emisor   = models.IntegerField()
    receptor = models.IntegerField()
    mensaje  = models.CharField(max_length=100)
    fecha    = models.DateTimeField(auto_now_add=True)
    hora     = models.TimeField(auto_now_add=True)
