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

class interesses(models.Model):
    nome = models.CharField(max_length=255)

class amigos(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.CharField(max_length=3000)

class vouchers(models.Model):
    nome = models.CharField(max_length=255)
    decricao = models.CharField(max_length=455)
    expirado = models.CharField(max_length=255)
    foto = models.CharField(max_length=3000)

class chat(models.Model):
    nome = models.CharField(max_length=255)
    mensagem = models.CharField(max_length=100)
    foto = models.CharField(max_length=3000)
    lidas = models.CharField(max_length=255)

class linkService(models.Model):
    nome = models.CharField(max_length=1024)

class isDebug(models.Model):
    nome = models.CharField(max_length=1024)

class skin(models.Model):
    imagemSpash = models.CharField(max_length=3000)
    imagemCapa = models.CharField(max_length=3000)
    cor1 = models.CharField(max_length=22)
    cor2 = models.CharField(max_length=22)
    cor3 = models.CharField(max_length=22)
    cor4 = models.CharField(max_length=22)
    cor5 = models.CharField(max_length=22)
    cor6 = models.CharField(max_length=22)
    cor7 = models.CharField(max_length=22)
    cor8 = models.CharField(max_length=22)
    cor9 = models.CharField(max_length=22)
    cor10 = models.CharField(max_length=22)