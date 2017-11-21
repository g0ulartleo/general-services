from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from dashboard.models import Client


class ClientView(ListView):
    def get(self, request, **kwargs):
        return render(request, 'clients.html')

    def post(self, request, **kwargs):
        return HttpResponseRedirect("/clients")
