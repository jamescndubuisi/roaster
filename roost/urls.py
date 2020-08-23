from django.urls import path
from .views import homepage, process, pre_schedule_view, pre_schedule_list

urlpatterns = [
    path('', homepage),
    path('process',process),
    path('see/<int:identity>',pre_schedule_view),
    path('see',pre_schedule_list),
]
