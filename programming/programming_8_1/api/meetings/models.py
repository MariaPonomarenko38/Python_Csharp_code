from django.db import models

# Create your models here.


class OnlineMeeting(models.Model):
    date = models.DateField(verbose_name='date', db_index=True, max_length=10)
    start_time = models.TimeField(verbose_name='start_time', db_index=True, max_length=5)
    end_time = models.TimeField(verbose_name='end_time', db_index=True, max_length=5)
    meeting_url = models.URLField(verbose_name='meeting_url', db_index=True, max_length=200)
    owner_first_name = models.CharField(verbose_name='Owner First Name', db_index=True, max_length=50, default='')
    owner_last_name = models.CharField(verbose_name='Owner Last Name', db_index=True, max_length=50, default='')
    participant_first_name = models.CharField(verbose_name='Participant First Name', db_index=True, max_length=50, default='')
    participant_last_name = models.CharField(verbose_name='Participant Last Name', db_index=True, max_length=50, default='')