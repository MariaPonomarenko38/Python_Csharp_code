from django.db import models
from django.contrib.auth import get_user_model
from api.meeting.models import Meeting

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="order_meetings")
    meeting = models.ManyToManyField(Meeting) #, related_name="user_meetings")
    ordered_date = models.DateField(auto_now=True)