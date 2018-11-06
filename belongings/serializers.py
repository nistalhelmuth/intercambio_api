from rest_framework import serializers
from . import models

class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = '__all__'
