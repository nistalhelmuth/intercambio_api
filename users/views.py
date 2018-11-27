from rest_framework import viewsets
from rest_framework import permissions
from . import models, serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserSerializerNoPassword
        return serializers.UserSerializer
