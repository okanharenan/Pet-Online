#from termios import CDSUSP
from reservas.models import ReservaModel, PetShop
from base.models import ContatoModel
import datetime
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)


class PetShopRelatedFieldsCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetShopNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data
    
class PetShopSerializer(ModelSerializer):
    reserva = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='Api:reservas-detail'
    )
    class Meta:
        model = PetShop
        fields = '__all__'
        

class PetShopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = PetShop
        fields = '__all__'

class ReservaModelSerializer(ModelSerializer):
    petshop = PetShopRelatedFieldsCustomSerializer(
        queryset=PetShop.objects.all(),
        read_only=False,
    )

    def validate_data(self,value):
        hoje = datetime.date.today()
        if value < hoje:
            ValidationError(f'{value} é uma data do passado, tente colocar uma data atual!')
        return value



    class Meta:
        model = ReservaModel
        fields = '__all__'

class ContatoModelSerializer(ModelSerializer):
    class Meta:
        model = ContatoModel
        fields = '__all__'