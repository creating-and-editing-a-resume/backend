from django.contrib import admin

from .models import Resume, Skills, WebLink


class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "position",
    )
    search_fields = (
        "author__last_name",
        "email",
    )
    list_filter = ("author", "position", "skills")


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Skills)
admin.site.register(WebLink)
