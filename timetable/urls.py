from django.urls import path
from timetable.views import main_page_view, two_weeks_view, pair_view


urlpatterns = [
    path('', main_page_view, name="main_page_view"),
    path('weeks/<int:group_id>/', two_weeks_view, name='two_weeks_view'),
    path('lesson/<int:pair_id>', pair_view, name='pair_view')
]
