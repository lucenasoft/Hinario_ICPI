from django.db import models

# Create your models here.

class Hinos(models.Model):
    titulo = models.CharField(max_length=100,verbose_name='Titulo')
    hino = models.TextField(verbose_name='Hino')

    def __str__(self):
        return self.titulo
