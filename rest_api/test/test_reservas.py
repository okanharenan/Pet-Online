from model_bakery import baker
from rest_framework.test import APIClient
from reservas.models import ReservaModel, PetShop
from rest_api.serializers import PetShopSerializer
import datetime
import pytest


@pytest.fixture
def agendamento():
    return baker.make(ReservaModel)

@pytest.fixture
def dados_agendamento_errado():
    ontem = datetime.date.today() + datetime.timedelta(days=1)
    petshop = baker.make(PetShop)
    return {
        'nome': 'nome teste', 'email':'email@teste.com', 'nome_pet':'pet test',
        'data': ontem, 'turno': 'manha', 'tamanho_pet':0, 'observacoes':'teste',
        'petshop':petshop.pk,
    }



@pytest.mark.django_db
def test_todos_agendamentos(agendamento):
    cliente = APIClient()
    resposta = cliente.get('/Api/agendamento')
    assert len(resposta.data['results']) == 1


