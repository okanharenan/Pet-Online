
from django.contrib import admin
from django.urls import path,include
from base.views import inicio,Contato, imagem
from rest_api.serializers import ReservaModelSerializer
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name="inicio"),
    path('contato/', Contato, name="contato"),
    path('fotos/', imagem , name="fotos"),
    path('criar/', include('reservas.urls', namespace="reserva")),
    path('Api/', include('rest_api.urls', namespace="agendamento"))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)