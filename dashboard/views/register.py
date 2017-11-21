from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class RegisterView(ListView):
    def get(self, request, **kwargs):
        return render(request, 'register.html')

    def post(self, request, **kwargs):
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        login(request, user)

        return HttpResponseRedirect("/dashboard")
