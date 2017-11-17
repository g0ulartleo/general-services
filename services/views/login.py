from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login

class LoginView(ListView):

    def get(self, request, **kwargs):
        data = {
            'error': False
        }
        return render(request, 'login.html', data)

    def post(self, request, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/dashboard")
        data = {
            'error':True
        }
        return render(request, 'login.html', data)

