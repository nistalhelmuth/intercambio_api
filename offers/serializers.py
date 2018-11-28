from rest_framework import serializers
from users.serializers import UserSerializer
from belongings.serializers import BelongingSerializer
from . import models


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        fields = '__all__'


class OfferSerializerFull(serializers.ModelSerializer):
    offered_by = UserSerializer()

    class Meta:
        model = models.Offer
        fields = '__all__'


class BelongingsPerOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BelongingsPerOffer
        fields = '__all__'


class BelongingsPerOfferSerializerFull(serializers.ModelSerializer):
    belonging = BelongingSerializer()

    class Meta:
        model = models.BelongingsPerOffer
        fields = '__all__'
