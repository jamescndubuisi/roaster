from django.urls import path
from .views import homepage, process, pre_schedule_view, pre_schedule_list, generate

urlpatterns = [
    path('', homepage),
    path('process',process),
    path('view-schedules/<int:identity>',pre_schedule_view, name = "schedules"),
    path('view-schedules',pre_schedule_list),
    path('generate',generate),
]
