from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        u = self.create_user(email,
                        name=name,
                        password=password,
                    )
        u.is_admin = True
        u.save(using=self._db)
        return u

class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False,
        default='',
    )
    name = models.CharField(
        max_length=90, 
        blank=False, 
        default=''
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0]

    def __str__(self):
        return self.email

