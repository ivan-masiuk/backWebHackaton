from django.urls import path
from app.views import main_page, group_weeks, lesson_page


urlpatterns = [
    path('', main_page, name="main_page"),
    path('weeks/<int:group_id>/', group_weeks, name='group_weeks'),
    path('lesson/<int:tutor_id>/<int:lesson_id>/', lesson_page, name='lesson')
]
