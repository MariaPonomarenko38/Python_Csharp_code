import jwt
from django.db import models
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class OnlineMeeting(models.Model):
    date = models.DateField(verbose_name='date', db_index=True, max_length=10)
    start_time = models.TimeField(verbose_name='start_time', db_index=True, max_length=5)
    end_time = models.TimeField(verbose_name='end_time', db_index=True, max_length=5)
    meeting_url = models.URLField(verbose_name='meeting_url', db_index=True, max_length=200)
    owner_first_name = models.CharField(verbose_name='Owner First Name', db_index=True, max_length=50, default='')
    owner_last_name = models.CharField(verbose_name='Owner Last Name', db_index=True, max_length=50, default='')
    participant_first_name = models.CharField(verbose_name='Participant First Name', db_index=True, max_length=50, default='')
    participant_last_name = models.CharField(verbose_name='Participant Last Name', db_index=True, max_length=50, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)