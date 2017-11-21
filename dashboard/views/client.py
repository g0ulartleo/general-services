from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from dashboard.models import Client


class ClientView(LoginRequiredMixin, ListView):

    def get(self, request, **kwargs):
        data = {}
        if 'id' in kwargs:
            try:
                client = Client.objects.get(id=kwargs['id'])
            except Client.DoesNotExist:
                return HttpResponseRedirect('/dashboard/client')
            else:
                if client.owner != request.user:
                    return HttpResponseRedirect('/dashboard/client')

            data['client'] = client
            return render(request, 'client-detail.html', data)
        else:
            data['clients'] = Client.objects.filter(owner=request.user)
            return render(request, 'client-list.html', data)

    def post(self, request, **kwargs):
        return HttpResponseRedirect("/client")
