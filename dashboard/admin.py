from django.contrib import admin

from .models import Client, User, Service

admin.site.register(Client)
admin.site.register(User)
admin.site.register(Service)
