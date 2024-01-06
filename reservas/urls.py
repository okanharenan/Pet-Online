from django.urls import path
from reservas.views import criar_reserva

app_name = "reserva"

urlpatterns= [
    path('reservas/', criar_reserva, name="reserva")
]