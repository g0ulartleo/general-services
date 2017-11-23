from django.db import models
from django.utils import timezone


class Client(models.Model):
    owner = models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=200, null=False)
    cpf = models.BigIntegerField(null=True, blank=True)
    primary_phone_number = models.CharField(max_length=15, blank=True)
    secondary_phone_number = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s (%s)' % (self.first_name, self.last_name, self.owner)
