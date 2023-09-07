from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        # print(request.GET)
        # print(self.value()) <QueryDict: {'word': ['great']}> 이렇게 나오는 위 print 결과값에서 'great'만
        word = self.value()
        if word:
            return reviews.filter(
                payload__contains=word
            )  # 이렇게 하면 admin 페이지 오른쪽 filter 중 'great'를 클릭하면 'great'를 포함한 review만 남고 사라진다.
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
