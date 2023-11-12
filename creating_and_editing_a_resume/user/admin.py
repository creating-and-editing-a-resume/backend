from django.contrib import admin
from user.models import about, courses, education, projects, user, work


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
    )
    search_fields = ("email", "last_name", "date_joined")
    list_filter = ("first_name", "city", "date_joined")


class EducationAdmin(admin.ModelAdmin):
    list_display = ("id", "university", "grade", "speciality", "student")
    search_fields = ("university", "grade", "speciality")
    list_filter = ("end_date", "start_date", "university")


class CoursesAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "name", "date", "student")
    search_fields = ("company", "name", "date")
    list_filter = ("company", "name", "date")


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


admin.site.register(user.ResumeUser, UserAdmin)
admin.site.register(education.Education, EducationAdmin)
admin.site.register(work.EmploymentHistory, EmploymentAdmin)
admin.site.register(about.Information)
admin.site.register(courses.Courses, CoursesAdmin)
admin.site.register(projects.Projects)
