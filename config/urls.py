"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# rooms import 방법1 : from rooms.views import say_hello
# rooms import 방법2 : from rooms import views  ---> path("rooms", views.say_hello)
# 방법2의 단점. 다른 모델 ex) users에도 똑같이 적용하면 이름이 겹친다.
# 이 경우 해결 방법: from users import views as users_views  ---> path("api/v1/어쩌구", room_views.say_hello)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rooms/", include("rooms.urls")),
    # path("api/v1/categories", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
