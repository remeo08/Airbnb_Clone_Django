from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerializer(
        read_only=True  # room을 생성할 때, serializer는 owner에 대한 정보를 요구하지 않음.
    )  # owner field의 경우 tinyuserserializer를 실행하라.
    amenities = AmenitySerializer(
        read_only=True,
        many=True,
    )  # many = True는 array
    category = CategorySerializer(
        read_only=True,
    )
    
    rating = serializers.SerializerMethodField()   # potato 필드의 값을 계산할 method를 만들거다.

    class Meta:
        model = Room
        fields = "__all__"
        # depth = 1   모든 정보가 확장되어 보임

	def get_rating(self, room):   
		return room.rating()


class RoomListSerializer(ModelSerializer):

    rating = serializers.SerializerMethodField()   # potato 필드의 값을 계산할 method를 만들거다.


    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating"
        )
    
    	def get_rating(self, room):   
		return room.rating()
