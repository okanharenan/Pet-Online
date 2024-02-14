
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from reservas.models import ReservaModel, PetShop
from rest_api.serializers import ReservaModelSerializer, ContatoModelSerializer, PetShopNestedModelSerializer
from rest_framework.decorators import action
from base.models import ContatoModel
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reservas.models import ReservaModel, PetShop
from rest_api.serializers import (
    ReservaModelSerializer,
    ContatoModelSerializer,
    PetShopSerializer,
)

class AgendamentoModelViewSet(ModelViewSet):
    """
    ViewSet para operações CRUD em ReservaModel.
    """
    serializer_class = ReservaModelSerializer
    queryset = ReservaModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class ContatoModelViewSet(ModelViewSet):
    """
    ViewSet para operações CRUD em ContatoModel.
    """
    serializer_class = ContatoModelSerializer
    queryset = ContatoModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class PetShopModelViewSet(ReadOnlyModelViewSet):
    queryset = PetShop.objects.all()
    serializer_class = PetShopSerializer

@api_view(['GET', 'POST', 'PUT'])
def hello_world(request):
    """
    Exemplo de função de visualização para a rota 'hello_world'.
    """
    if request.method == "POST":
        name = request.data.get("name")
        return Response({'mensagem': f'Hello, {name}'})

    return Response({'hello': 'World_API'})
