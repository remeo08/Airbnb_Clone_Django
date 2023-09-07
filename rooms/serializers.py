from rest_framework import serializers
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(serializers.ModelSerializer):
    owner = TinyUserSerializer(
        read_only=True
    )  # owner를 serialize할 경우 tinyuserserializer를 사용해라.
    amenities = AmenitySerializer(
        read_only=True,
        many=True,
    )  # many = True는 array
    category = CategorySerializer(
        read_only=True,
    )

    rating = serializers.SerializerMethodField()  # potato 필드의 값을 계산할 method를 만들거다.
    is_owner = serializers.SerializerMethodField()  # potato 필드의 값을 계산할 method를 만들거다.
    reviews = ReviewSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Room
        fields = "__all__"
        # depth = 1   모든 정보가 확장되어 보임

    def get_rating(self, room):
        print(self.context)
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user


class RoomListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()  # potato 필드의 값을 계산할 method를 만들거다.

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
        )

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        print(request)
        return room.owner == request.user
