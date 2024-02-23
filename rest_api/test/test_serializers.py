import pytest
from model_bakery import baker
from reservas.models import ReservaModel
from reservas.models import PetShop
from rest_api.serializers import ReservaModelSerializer
import datetime

@pytest.fixture
def dados_agendamento_errado():
    ontem = datetime.date.today() - datetime.timedelta(days=1)
    petshop = baker.make(PetShop)
    return {
        'nome': 'nome teste', 'email':'email@teste.com', 'nome_pet':'pet test',
        'data': ontem, 'turno': 'Manhã', 'tamanho_pet':0, 'observacoes':'teste',
        'petshop':petshop.pk,
    }

@pytest.mark.django_db
def test_data_agendamento_invalida(dados_agendamento_errado):
    serializer = ReservaModelSerializer(data=dados_agendamento_errado)
    assert not serializer.is_valid()