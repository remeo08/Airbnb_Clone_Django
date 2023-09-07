from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
# 3개의 매개변수 필요(이 액션을 호출하는 클래스, request 객체, queryset)
# (이 액션을 호출한 유저 정보를 가지고 있는 request 객체)
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    def total_amenities(self, room):
        return room.amenities.count()

    search_fields = ("owner__username",)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
