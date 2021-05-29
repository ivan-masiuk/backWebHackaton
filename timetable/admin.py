from django.contrib import admin
from timetable.models import Subject, Group, Pair, Week, DayOfTheWeek

admin.site.register(Pair)
admin.site.register(Week)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(DayOfTheWeek)
