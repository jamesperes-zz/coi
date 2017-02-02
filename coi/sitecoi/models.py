from django.db import models

from PIL import Image

from .choices import FAB, TIPO


class Armas(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(('Tipo de Arma '), max_length=50, choices=TIPO)
    fabricante = models.CharField(('Fabricante'), max_length=50, choices=FAB)
    imagem = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.nome
