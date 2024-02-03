
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from reservas.models import ReservaModel
from rest_api.serializers import ReservaModelSerializer, ContatoModelSerializer
from rest_framework.decorators import action
from base.models import ContatoModel
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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

 

@api_view(['GET','POST','PUT'])
def  hello_world(request):
    if request.method == "POST":
        return Response({'mensagem': f'Hello, {request.data.get("name")}'}) 
    
    return Response({'hello': 'World_API'})



