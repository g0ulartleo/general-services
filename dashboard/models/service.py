from django.db import models
from django.utils import timezone


class Service(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    base_price = models.FloatField(null=False)

    def __str__(self):
        return '%s (%s)' % (self.name, self.owner)
