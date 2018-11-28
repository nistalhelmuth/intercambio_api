from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from . import models, serializers


class BelongingViewSet(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer

    @action(methods=['GET'], detail=False, url_path='from_user')
    def from_user(self, request, pk=None):
        user_id = request.query_params.get('user')
        belongings = models.Belonging.objects.filter(belongs_to__id=user_id)
        return Response(serializers.BelongingSerializer(belongings, many=True).data)
