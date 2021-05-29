from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404
from django.contrib import messages

from app.models import Week, Group


# def one_week_view(request, wid):
#     current_week = get_object_or_404(Week, id=wid)
#
#     name_week = current_week.name
#     group = current_week.group
#     days = current_week.days
#
#     context = {
#         "name_week": name_week,
#         "group": group,
#         "days": days,
#     }
#     return render(request, '', context)


def test(request):

    action = request.POST.get('action')

    if request.POST and action == 'Мій розклад':
        name_group = request.POST['name_group']
        groups = Group.objects.all()
        for group in groups:
            if group.name == name_group:
                return redirect('')
        else:
            return redirect('')
