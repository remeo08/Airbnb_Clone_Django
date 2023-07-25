from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="medias",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="medias",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):
    file = models.ImageField()
    experience = models.OneToOneField(
        "experiences.Experience", on_delete=models.CASCADE
    )

    def __str__(self):
        return "Video File"
