from django.contrib import admin

from .models import (Resume, Skills, WebLink)


admin.site.register(Resume)
admin.site.register(Skills)
admin.site.register(WebLink)