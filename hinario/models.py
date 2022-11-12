from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hino(models.Model):
    titulo = models.CharField(max_length=100,verbose_name='Titulo')
    hino = models.TextField(verbose_name='Hino')

    def __str__(self):
        return self.titulo
