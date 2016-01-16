from servidores.models import Servidor
from servidores.serializers import ServidorSerializer, UserSerializer
from servidores.permissions import IsAdminOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

# Classe para tratamento de listagem ou cadastro baseado em request
class ServidorListagem(generics.ListCreateAPIView):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly)

    # override de método para atualizar o criador do servidor 
    # baseado no usuario da request passada
    def perform_create(self, serializer):
        serializer.save(criador=self.request.user)
    
# Classe para tratamento de update, find e delete baseado em request
class ServidorDetalhes(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly)
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer