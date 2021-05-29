from django.contrib import messages
from django.shortcuts import render, redirect

from timetable.models import Group


def main_page_view(request):
    action = request.POST.get('action')

    if request.POST and action == 'Знайти':
        name_group = request.POST['name_group']
        groups = Group.objects.all()
        for group in groups:
            if group.name == name_group:
                return redirect('group_weeks', group_id=group.id)
        else:
            messages.warning(request, "на жаль, такої групи не існує!")
            return redirect('main_page')

    return render(request, 'start-page.html')


def two_weeks_view(request):
    pass


def pair_view(request):
    pass