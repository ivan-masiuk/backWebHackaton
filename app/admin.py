from django.contrib import admin
from app.models import (Group,
                        Week,
                        Lesson,
                        Day,
                        Subject)

admin.site.register(Group)
admin.site.register(Week)
admin.site.register(Lesson)
admin.site.register(Day)
admin.site.register(Subject)
