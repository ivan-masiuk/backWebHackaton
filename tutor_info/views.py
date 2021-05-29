from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect

from tutor_info.models import VoteStudent, TutorStatistic
from account.models import Profile


def tutor_info_view(request, tutor_profile_id):
    tutor = get_object_or_404(Profile, id=tutor_profile_id)

    action = request.POST.get('action')

    if request.POST and action == 'Оцінити тьютора':
        return redirect('vote_student_view', tutor_id=tutor_profile_id)

    context = {
        'tutor': tutor,
    }
    return render(request, 'tutor_info/tutor_info.html', context)


@login_required
def vote_student_view(request, tutor_profile_id):
    tutor = get_object_or_404(Profile, id=tutor_profile_id)
    action = request.POST.get('action')

    if request.POST and action == 'Оцінити тьютора':
        student = Profile.objects.get(user=request.user)
        VoteStudent.objects.create(punctuality=request.POST['punctuality'],
                                   loyalty=request.POST['loyalty'],
                                   grading=request.POST['grading'],
                                   tutor_fk=tutor,
                                   student_fk=student)
        messages.success(request, "Вітаємо, Ваш голос враховано! Дякуємо!")
        return redirect('tutor_info_pass', tutor_id=tutor_profile_id)

    # form_for_student =

    context = {
        # 'form_for_student': form_for_student,
    }
    return render(request, 'tutor_info/student_vote_form.html', context)
