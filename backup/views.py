from django.contrib.auth.models import User

from backup.models import Backup
from backup.serializers import BackupSerializer, UserSerializer
from backup.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions, renderers, viewsets, status

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'backups': reverse('backup-list', request=request, format=format)
    })


class BackupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Backup.objects.all()
    serializer_class = BackupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        backup = self.get_object()
        return Response(backup.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteViewSet(APIView):
    def delete(self, request, format=None):
        snippets = Backup.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
