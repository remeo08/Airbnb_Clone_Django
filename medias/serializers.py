from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Photo


class PhotoSerializer(ModelSerializer):
    # hello = serializers.CharField(max)

    class Meta:
        model = Photo
        fields = (
            "pk",
            "file",
            "description",
        )


def create(self, validated_data):
    return super().create(validated_data)
