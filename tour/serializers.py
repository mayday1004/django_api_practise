from rest_framework import serializers, status
from rest_framework.validators import ValidationError
from .models import Tour


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "duration",
            "price",
        ]
