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
    splash_image = models.CharField(max_length=3000)
    background_image = models.CharField(max_length=3000)
    nome = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    white_color = models.CharField(max_length=22)
    black_color = models.CharField(max_length=22)
    firstLinearColor = models.CharField(max_length=22)
    secondLinearColor = models.CharField(max_length=22)
    firstFacebookLinear = models.CharField(max_length=22)
    secondFacebookLinear = models.CharField(max_length=22)
    textFriendsColor = models.CharField(max_length=22)
    customBackgroundColor = models.CharField(max_length=22)
    customMainColor = models.CharField(max_length=22)


class testandoRest(models.Model):
    name = models.CharField(max_length=255)

class testConnection(models.Model):
    test = models.CharField(max_length=255)
    name2 = models.ForeignKey(testandoRest, on_delete=models.CASCADE)

class voucher(models.Model):
    imageUrl = models.CharField(max_length=3000)
    nameVoucher = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    partner = models.CharField(max_length=255)
    typeVoucher = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)
    minBuy = models.CharField(max_length=255)
    maxBuy = models.CharField(max_length=255)
    cMin = models.CharField(max_length=255)
    valitityDe = models.CharField(max_length=255)
    valitityAte = models.CharField(max_length=255)
    rescue = models.CharField(max_length=255)
    useOnly = models.CharField(max_length=255)
    visibility = models.IntegerField(default=0)