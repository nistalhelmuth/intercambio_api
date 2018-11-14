from rest_framework import serializers
from users.serializers import UserSerializer
from . import models

class OfferSerializer(serializers.ModelSerializer):
    offered_by = UserSerializer()   
    class Meta:
        model = models.Offer
        fields = '__all__'
