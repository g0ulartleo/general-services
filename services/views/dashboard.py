from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login

class DashboardView(ListView):
    pass
