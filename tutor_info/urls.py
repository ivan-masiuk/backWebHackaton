from django.urls import path

from tutor_info.views import (tutor_info_view,
                              all_tutors_view,
                              vote_student_view)


urlpatterns = [
    path('', all_tutors_view, name="all_tutors_view"),
    path('tutor-info/<int:tutor_profile_id>/', tutor_info_view, name="tutor_info_view"),
    path('student-vote/<int:tutor_profile_id>/', vote_student_view, name="vote_student_view"),

]
