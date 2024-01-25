from rest_framework.serializers import ModelSerializer
from reservas.models import ReservaModel
from base.models import ContatoModel
from datetime import date

class ReservaModelSerializer(ModelSerializer):
    class Meta:
        model = ReservaModel
        fields = '__all__'

      

class ContatoModelSerializer(ModelSerializer):
    class Meta:
        model = ContatoModel
        fields = '__all__'