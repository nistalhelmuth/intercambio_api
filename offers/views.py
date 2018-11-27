from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from posts.models import Post
from . import models, serializers

class OfferViewSet(viewsets.ModelViewSet):
    queryset = models.Offer.objects.all()
    serializer_class = serializers.OfferSerializer

    @action(methods=['GET'], detail=False, url_path='by_post')
    def by_post(self, request, pk=None):
        post_id = request.query_params.get('post')
        post = Post.objects.get(pk=post_id)
        offers = models.Offer.objects.filter(offered_in=post).order_by('date')
        return Response(serializers.OfferSerializer(offers, many=True).data)

class BelongingsPerOfferViewSet(viewsets.ModelViewSet):
    queryset = models.BelongingsPerOffer.objects.all()
    serializer_class = serializers.BelongingsPerOfferSerializer

    @action(methods=['GET'], detail=False, url_path='by_offer')
    def by_offer(self, request, pk=None):
        offer_id = request.query_params.get('offer')
        offer = models.Offer.objects.get(pk=offer_id)
        belongings = models.BelongingsPerOffer.objects.filter(offer=offer)
        return Response(serializers.BelongingsPerOfferSerializer(belongings, many=True).data)
