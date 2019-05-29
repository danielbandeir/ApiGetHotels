from rest_framework import serializers
from .models import hotel, pessoa, comentario, interesses, amigos, vouchers, chat, linkService, isDebug, skin, testConnection, voucher


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

class linkServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = linkService
        fields='__all__'
    
class isDebugSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = isDebug
        fields = "__all__"

class skinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = skin
        fields = "__all__"

class testConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = testConnection
        fields = "__all__"
    
class voucherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = voucher
        fields = "__all__"