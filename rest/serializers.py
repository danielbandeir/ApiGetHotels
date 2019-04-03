from rest_framework import serializers
from .models import hotel, pessoa

class hotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hotel
        fields = '__all__'

class pessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pessoa
        fields = '__all__'