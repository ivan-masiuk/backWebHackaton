from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect

from django.core.exceptions import ObjectDoesNotExist

from tutor_info.models import VoteStudent, TutorStatistic
from account.models import Profile

from tutor_info.forms import StudentVoteForm


def all_tutors_view(request):
    users = User.objects.filter(groups__name='Tutor')

    context = {
        'users': users,
    }
    return render(request, 'tutor_info/all_tutors.html', context)


def tutor_info_view(request, tutor_profile_id):
    tutor = get_object_or_404(Profile, id=tutor_profile_id)

    # check is tutor_profile_id == Tutor
    if not checkTutor(tutor.user):
        messages.warning(request, 'Викладача з таким ID не існує!')
        return redirect('main_page_view')

    action = request.POST.get('action')

    if request.POST and action == 'Оцінити тьютора':
        return redirect('vote_student_view', tutor_profile_id=tutor_profile_id)

    # try to get TutorStatistic
    statistic_tutor = getTutorStatisticByTutor(tutor)

    context = {
        'tutor': tutor,
        'statistic_tutor': statistic_tutor,
    }
    return render(request, 'tutor_info/tutor_info.html', context)


@login_required
def vote_student_view(request, tutor_profile_id):
    tutor = get_object_or_404(Profile, id=tutor_profile_id)

    # check is tutor_profile_id == Tutor
    if not checkTutor(tutor.user):
        messages.warning(request, 'Викладача з таким ID не існує!')
        return redirect('main_page_view')

    action = request.POST.get('action')

    if request.POST and action == 'Оцінити тьютора':
        student = Profile.objects.get(user=request.user)

        # get data from POST
        punctuality = int(request.POST['punctuality'])
        loyalty = int(request.POST['loyalty'])
        grading = int(request.POST['grading'])
        relevance = int(request.POST['relevance'])
        positive = int(request.POST['positive'])

        # add VoteStudent
        VoteStudent.objects.create(punctuality=punctuality,
                                   loyalty=loyalty,
                                   grading=grading,
                                   positive=positive,
                                   relevance=relevance,
                                   tutor_profile_fk=tutor,
                                   student_profile_fk=student)

        # try to get TutorStatistic
        statistic_tutor = getTutorStatisticByTutor(tutor)

        # math new TutorStatistic
        qty_votes = len(tutor.votes_by_student.all())
        statistic_tutor.punctuality = (statistic_tutor.punctuality + punctuality) / qty_votes
        statistic_tutor.loyalty = (statistic_tutor.loyalty + loyalty) / qty_votes
        statistic_tutor.grading = (statistic_tutor.grading + grading) / qty_votes
        statistic_tutor.relevance = (statistic_tutor.relevance + relevance) / qty_votes
        statistic_tutor.positive = (statistic_tutor.positive + positive) / qty_votes
        statistic_tutor.save()

        messages.success(request, "Вітаємо, Ваш голос враховано! Дякуємо!")
        return redirect('tutor_info_view', tutor_profile_id=tutor_profile_id)

    return render(request, 'tutor_info/student_vote_form.html')


def getTutorStatisticByTutor(tutor):
    try:
        statistic_tutor = TutorStatistic.objects.filter(tutor_profile_fk=tutor)[0]
    except ObjectDoesNotExist:
        statistic_tutor = TutorStatistic.objects.create(tutor_profile_fk=tutor)
    except IndexError:
        statistic_tutor = TutorStatistic.objects.create(tutor_profile_fk=tutor)

    return statistic_tutor


def checkTutor(user):
    if user.groups.filter(name="Tutor").exists():
        return True
    else:
        return False
