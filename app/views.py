from app.models import Group, Lesson
from account.models import Tutor
from django.shortcuts import render, redirect


def main_page(request):
    return render(request, 'start-page.html')


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


def test(request):
    action = request.POST.get('action')

    if request.POST and action == 'Знайти':
        name_group = request.POST['name_group']
        groups = Group.objects.all()
        for group in groups:
            if group.name == name_group:
                return redirect('')
        else:
            return redirect('')


def lesson_page(request, tutor_id, lesson_id):
    tutor = Tutor.objects.get(id=tutor_id)
    lesson = Lesson.objects.get(id=lesson_id)
    context = {'tutor': tutor,
               'lesson': lesson}

    return render(request, 'lesson.html', context)
