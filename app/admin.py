from django.contrib import admin
from app.models import (Group,
                        Week,
                        Tutor,
                        Lesson,
                        Day)

admin.site.register(Group)
admin.site.register(Week)
admin.site.register(Tutor)
admin.site.register(Lesson)
admin.site.register(Day)
