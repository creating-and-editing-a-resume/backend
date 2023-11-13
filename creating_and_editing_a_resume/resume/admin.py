from django.contrib import admin

from .models import Resume, Skills, WebLink


@admin.register(Resume)
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


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "skill",
        "profession",
    )
    search_fields = (
        "skill",
        "profession",
    )
    list_filter = ("profession",)


@admin.register(WebLink)
class WebLinkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "web_page",
    )
    search_fields = (
        "name",
        "web_page",
    )
    list_filter = ("name",)
