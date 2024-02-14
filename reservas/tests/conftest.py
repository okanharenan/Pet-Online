from model_bakery import baker
import pytest
from reservas.models import ReservaModel, PetShop
from datetime import date 


@pytest.fixture
def reserva():
    data  = date(2024,1,14)
    return baker.make(
        ReservaModel,
        nome = 'Tom',
        #data  = date.today(),
        data = data,
        turno = 'Manhã',

    )

@pytest.fixture
def petshop():
    return baker.make(PetShop, id=2)