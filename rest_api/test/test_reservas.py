from model_bakery import baker
from rest_framework.test import APIClient
from reservas.models import ReservaModel, PetShop
from rest_api.serializers import PetShopSerializer
import pytest


@pytest.fixture
def agendamento():
    return baker.make(ReservaModel)


@pytest.mark.django_db
def test_todos_agendamentos(agendamento):
    cliente = APIClient()
    resposta = cliente.get('/Api/agendamento')
    assert len(resposta.data['results']) == 1