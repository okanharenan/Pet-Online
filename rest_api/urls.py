from django.urls import path,include
from rest_framework.routers import SimpleRouter
from rest_api.serializers import ReservaModelSerializer
from rest_api.views import AgendamentoModelViewSet, hello_world, ContatoModelViewSet, PetShopModelViewSet


app_name = "agendamento"

router = SimpleRouter(trailing_slash=False)
router.register('agendamento', AgendamentoModelViewSet)
router.register('contatos', ContatoModelViewSet)
router.register('petshop', PetShopModelViewSet)




urlpatterns = [
    path('hello_api/', hello_world, name="hello_api"),
]

urlpatterns += router.urls