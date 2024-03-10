from rest_framework.test import APIClient
from model_bakery import baker
from reservas.models import PetShop
import pytest

@pytest.mark.django_db
def test_sem_petshop_salvo():
    cliente = APIClient()
    resposta = cliente.get('Api/petshop/')
    assert len(resposta.data['results']) == 0