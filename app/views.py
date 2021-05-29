from django.shortcuts import render
from app.models import Group


def main_page(request):
    return render(request, 'base.html')


def group_weeks(request, group_id):
    context = {}
    group = Group.objects.get(id=group_id)
    weeks = group.weeks.all()
    if weeks[0]:
        week_1 = weeks[0]
        context.update({'week_1': week_1})
    if weeks[1]:
        week_2 = weeks[1]
        context.update({'week_2': week_2})
    return render(request, 'weeks-page.html', context)
