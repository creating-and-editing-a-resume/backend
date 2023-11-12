from django.contrib import admin
from user.models import about, courses, education, projects, user, work

admin.site.register(user.ResumeUser)
admin.site.register(education.Education)
admin.site.register(work.EmploymentHistory)
admin.site.register(about.Information)
admin.site.register(courses.Courses)
admin.site.register(projects.Projects)
