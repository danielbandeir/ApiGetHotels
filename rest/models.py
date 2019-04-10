from django.db import models

class hotel(models.Model):
    nome = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    language = models.CharField(max_length=20)
    background_image = models.CharField(max_length=20000)
    maps_image = models.CharField(max_length=20000)

class pessoa(models.Model):
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=15)
    foto = models.CharField(max_length=20000)

class comentario(models.Model):
    nomePessoa = models.CharField(max_length=255)
    tempo = models.CharField(max_length=255)
    foto = models.CharField(max_length=20000)
    texto = models.CharField(max_length=255)