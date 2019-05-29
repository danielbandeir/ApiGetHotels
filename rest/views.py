from django.shortcuts import render
from rest_framework import viewsets
from .models import hotel, pessoa, comentario, interesses, amigos, vouchers, chat, linkService, isDebug, skin, testConnection, voucher
from .serializers import hotelSerializer, pessoaSerializer, comentarioSerializer, interessesSerializer, amigosSerializer, vouchersSerializer, chatSerializer, linkServiceSerializer, isDebugSerializer, skinSerializer, testConnectionSerializer, voucherSerializer


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

class linkServiceViewSet(viewsets.ModelViewSet):
    queryset = linkService.objects.all()
    serializer_class = linkServiceSerializer

class isDebugViewSet(viewsets.ModelViewSet):
    queryset = isDebug.objects.all()
    serializer_class = isDebugSerializer

class skinViewSet(viewsets.ModelViewSet):
    queryset = skin.objects.all()
    serializer_class = skinSerializer

class testConnectionViewSet(viewsets.ModelViewSet):
    queryset = testConnection.objects.all()
    serializer_class = testConnectionSerializer

class voucherViewSet(viewsets.ModelViewSet):
    queryset = voucher.objects.all()
    serializer_class = voucherSerializer