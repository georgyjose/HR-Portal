from django.db import models


# Create your models here.


class TimeSlot(models.Model):
    INTERVIEWER = "INTERVIEWER"
    CANDIDATE = "CANDIDATE"
    USER_TYPE_CHOICES = ((CANDIDATE, "candidate"), (INTERVIEWER, "interviewer"))

    name = models.CharField(max_length=30)
    email = models.EmailField()
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES)
    available_from = models.DateTimeField()
    available_to = models.DateTimeField()
