from django.contrib import messages
from django.shortcuts import render, redirect

from timetable.models import (Group,
                              Subject,
                              Week,
                              DayOfTheWeek,
                              Pair)


def main_page_view(request):
    action = request.POST.get('action')

    if request.POST and action == 'Знайти':
        name_group = request.POST['name_group']
        groups = Group.objects.all()
        for group in groups:
            if group.title == name_group:
                return redirect('two_weeks_view', group_id=group.id)
        else:
            messages.warning(request, "На жаль, такої групи не існує!")
            return redirect('main_page_view')

    return render(request, 'start-page.html')


def two_weeks_view(request, group_id):
    context = {}
    weeks = Group.objects.get(id=group_id).weeks.all()
    context.update({'weeks': weeks})
    return render(request, 'timetable/two-weeks-page.html', context)


def pair_view(request, pair_id):
    context = {}
    context.update({'pair': Pair.objects.get(id=pair_id)})

    return render(request, 'timetable/pair-page.html', context)
