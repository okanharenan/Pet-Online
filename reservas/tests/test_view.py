import pytest
from pytest_django.asserts import assertTemplateUsed 

@pytest.mark.django_db
def test_reserva_view_deve_retornar_template(client):

    response = client.get('/criar/reservas/')

    assert response.status_code == 200

    assertTemplateUsed(response, 'reserva.html')