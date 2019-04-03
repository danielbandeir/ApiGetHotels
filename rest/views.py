from django.shortcuts import render
from rest_framework import viewsets
from .models import hotel, pessoa
from .serializers import hotelSerializer, pessoaSerializer

class hotelViewSet(viewsets.ModelViewSet):
    queryset = hotel.objects.all()
    serializer_class = hotelSerializer

class pessoaViewSet(viewsets.ModelViewSet):
    queryset = pessoa.objects.all()
    serializer_class = pessoaSerializer