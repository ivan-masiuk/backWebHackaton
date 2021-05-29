from django.urls import path

from tutor_info.views import (tutor_info_view,
                              vote_student_view)


urlpatterns = [
    path('tutor-info/<int:tutor_profile_id>/', tutor_info_view, name="tutor_info_pass"),
    path('student-vote/<int:tutor_profile_id>/', vote_student_view, name="vote_student_view"),

]
