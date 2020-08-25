from django.urls import path
from .views import homepage, process, pre_schedule_view, pre_schedule_list, generate, edit_schedule

urlpatterns = [
    path('', homepage),
    path('process',process),
    path('view-schedules/<int:identity>',pre_schedule_view, name = "schedules"),
    path('edit/<int:identity>',edit_schedule, name = "edit"),
    path('view-schedules',pre_schedule_list),
    path('generate',generate),
]
