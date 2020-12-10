from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, first_name, last_name, email, password=None, is_active=True, is_staff=False, is_superuser=False):
        if not first_name:
            raise ValueError('First name should be set')
        if not last_name:
            raise ValueError('Last name should be set')
        if not email:
            raise ValueError('Email should be set')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, first_name, last_name, email, password=None):
        user = self._create_user(first_name, last_name, email, password=password, is_staff=True)

        return user

    def create_superuser(self, first_name, last_name, email, password=None):
        user = self._create_user(first_name, last_name, email, password=password, is_staff=True, is_superuser=True)
        return user