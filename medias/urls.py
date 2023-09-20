from django.urls import path
from .views import PhotoDetail

urlpatterns = [
    path("", PhotoDetail.as_view()),
]
