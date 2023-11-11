from django.contrib import admin

from .models import (ResumeUser, Education, EmploymentHistory, Information,
                     Courses, Projects,)


admin.site.register(ResumeUser)
admin.site.register(Education)
admin.site.register(EmploymentHistory)
admin.site.register(Information)
admin.site.register(Courses)
admin.site.register(Projects)
