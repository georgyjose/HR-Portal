from django.urls import path
from .views import InterviewerList, TimeSlotView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'timeslot', InterviewerList)

urlpatterns = [
    path('timeslot/<int:iid>/<int:cid>/', TimeSlotView.as_view()),
]

urlpatterns += router.urls
