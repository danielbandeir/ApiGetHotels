from django.shortcuts import render
from rest_framework import viewsets
from .models import hotel, pessoa, comentario, interesses, amigos, vouchers, chat
from .serializers import hotelSerializer, pessoaSerializer, comentarioSerializer, interessesSerializer, amigosSerializer, vouchersSerializer, chatSerializer


class hotelViewSet(viewsets.ModelViewSet):
    queryset = hotel.objects.all()
    serializer_class = hotelSerializer

class pessoaViewSet(viewsets.ModelViewSet):
    queryset = pessoa.objects.all()
    serializer_class = pessoaSerializer

class comentarioViewSet(viewsets.ModelViewSet):
    queryset = comentario.objects.all()
    serializer_class = comentarioSerializer

class interessesViewSet(viewsets.ModelViewSet):
    queryset = interesses.objects.all()
    serializer_class = interessesSerializer

class amigosViewSet(viewsets.ModelViewSet):
    queryset = amigos.objects.all()
    serializer_class = amigosSerializer

class vouchersViewSet(viewsets.ModelViewSet):
    queryset = vouchers.objects.all()
    serializer_class = vouchersSerializer

class chatViewSet(viewsets.ModelViewSet):
    queryset = chat.objects.all()
    serializer_class = chatSerializer