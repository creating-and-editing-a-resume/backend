from django.contrib import admin
from user.models import (
    about,
    courses,
    education,
    language,
    projects,
    user,
    work,
)


@admin.register(user.ResumeUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
    )
    search_fields = ("email", "last_name", "date_joined")
    list_filter = ("first_name", "city", "date_joined")


@admin.register(education.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("id", "university", "grade", "speciality", "student")
    search_fields = ("university", "grade", "speciality")
    list_filter = ("end_date", "start_date", "university")


@admin.register(courses.Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "name", "date", "student")
    search_fields = ("company", "name", "date")
    list_filter = ("company", "name", "date")


@admin.register(work.EmploymentHistory)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company",
        "position",
        "start_date",
        "end_date",
        "employee",
    )
    search_fields = ("company", "position", "date", "start_date", "end_date")
    list_filter = ("company", "position", "end_date")


@admin.register(about.Information)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(projects.Projects)
class ProjectsAdmin(admin.ModelAdmin):
    pass


@admin.register(language.Langeuage)
class LanguageAdmin(admin.ModelAdmin):
    pass
