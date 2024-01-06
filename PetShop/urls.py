
from django.contrib import admin
from django.urls import path,include
from base.views import inicio,Contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name="inicio"),
    path('contato/', Contato, name="contato"),
    path('criar/', include('reservas.urls', namespace="reserva"))
]
