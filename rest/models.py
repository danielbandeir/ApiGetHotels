from django.db import models

class hotel(models.Model):
    nome = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    language = models.CharField(max_length=20)
    background_image = models.CharField(max_length=20000)
    maps_image = models.CharField(max_length=20000)
