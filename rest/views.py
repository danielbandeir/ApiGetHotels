from django.shortcuts import render
from rest_framework import viewsets
from .models import hotel
from .serializers import hotelSerializer

class hotelViewSet(viewsets.ModelViewSet):
    queryset = hotel.objects.all()
    serializer_class = hotelSerializer