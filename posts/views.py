from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from categories.models import Category
from . import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    @action(methods=['GET'], detail=False, url_path='by_category')
    def by_category(self, request, pk=None):
        category_id = request.query_params.get('category')
        category = Category.objects.get(pk=category_id)
        posts = models.Post.objects.filter(category=category)
        return Response(serializers.PostSerializer(posts, many=True).data)
