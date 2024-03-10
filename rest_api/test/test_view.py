import pytest
from rest_framework.test import APIClient
import datetime
from model_bakery import baker
from reservas.models import PetShop, ReservaModel
from rest_api.serializers import PetShopSerializer


class TestView:


    @pytest.mark.django_db
    def test_todos_petshops(self):
        cliente = APIClient()
        resposta = cliente.get('/Api/petshop')
        assert len(resposta.data['results']) == 0

    @pytest.fixture
    def dados_agendamento(self):
        hoje = datetime.date.today()
        petshop = baker.make(PetShop)
        return {
        'nome': 'nome teste', 'email':'email@teste.com', 'nome_pet':'pet test',
        'data': hoje, 'turno': 'Manhã', 'tamanho_pet':0, 'observacoes':'teste',
        'petshop':petshop.pk,
        }
    
    @pytest.fixture
    def usuario(self):
        return baker.make('auth.User')
    
    @pytest.mark.django_db
    def test_criar_agendamento(self,dados_agendamento, usuario):
        cliente = APIClient()
        cliente.force_authenticate(usuario)
        resposta = cliente.post('/Api/agendamento', dados_agendamento)
        print(resposta)
        assert resposta.status_code == 201

    