from rest_framework import serializers
from .models import hotel

class hotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hotel
        fields = '__all__'