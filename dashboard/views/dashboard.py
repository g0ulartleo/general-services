from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login


class DashboardView(LoginRequiredMixin, ListView):
    login_url = '/login/'

    def get(self, request, **kwargs):
        return render(request, 'dashboard.html')
