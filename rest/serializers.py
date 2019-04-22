from rest_framework import serializers
from .models import hotel, pessoa, comentario, interesses, amigos, vouchers, chat


class hotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hotel
        fields = '__all__'

class pessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pessoa
        fields = '__all__'

class comentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = comentario
        fields = '__all__'

class interessesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = interesses
        fields = '__all__'

class amigosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = amigos
        fields = '__all__'

class vouchersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = vouchers
        fields ='__all__'

class chatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = chat
        fields = '__all__'