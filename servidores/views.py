from servidores.models import Servidor
from servidores.serializers import ServidorSerializer, UserSerializer
from servidores.permissions import IsAdminOrReadOnly
from rest_framework import permissions
from rest_framework.decorators import detail_route, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.views.generic import TemplateView

@api_view(['GET',])
def api_root(request, format=None):
    return Response({
        'usuarios': reverse('user-list', request=request, format=format),
        'servidores': reverse('servidor-list', request=request, format=format)
    })

class Index(TemplateView):
    template_name = "index.html"

# Viewset para realizar as operações de CRUD dos servidores
class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          IsAdminOrReadOnly)

    # override de método para atualizar o criador do servidor 
    # baseado no usuario da request passada
    def perform_create(self, serializer):
        serializer.save(criador=self.request.user)


# Viewset para reproduzir a listagem e detalhamento de usuários
class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer