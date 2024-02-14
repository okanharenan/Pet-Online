import pytest
from model_bakery import baker
from reservas.models import PetShop, ReservaModel

@pytest.mark.django_db
def test_deve_retornar_string_formatada(reserva):

    assert str(reserva) == 'Tom: 2024-01-14- Manhã'

@pytest.mark.django_db
def test_qtd_de_reserva_deve_retornar_numeros_de_reservas(petshop):
    baker.make(ReservaModel, _quantity=3, petshop=petshop)
    # Obtém a quantidade de reservas associadas ao PetShop
    qtd_reservas = ReservaModel.objects.filter(petshop=petshop).count()

    assert qtd_reservas == 3
