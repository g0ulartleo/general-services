from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from dashboard.forms import ClientForm
from dashboard.models import Client


class ClientView(LoginRequiredMixin, ListView):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'patch':
            return self.patch(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        return super(ClientView, self).dispatch(*args, **kwargs)

    def _get_client_by_id(self, request, _id):
        try:
            client = Client.objects.get(id=_id)
        except Client.DoesNotExist:
            return HttpResponseRedirect('/dashboard/client')
        else:
            if client.owner != request.user:
                return HttpResponseRedirect('/dashboard/client')
        return client

    def get(self, request, **kwargs):
        data = {}
        if 'id' in kwargs:
            data = {
                'form': ClientForm(),
            }
            if kwargs['id'] != '0':
                client = self._get_client_by_id(request, kwargs['id'])
                data['form'] = ClientForm(instance=client)
                data['client'] = client
            return render(request, 'client-detail.html', data)
        else:
            data['clients'] = Client.objects.filter(owner=request.user)
            return render(request, 'client-list.html', data)

    def patch(self, request, **kwargs):
        if 'id' in kwargs:
            client = self._get_client_by_id(request, kwargs['id'])
            post = request.POST.copy()
            post['owner'] = request.user.id
            form = ClientForm(post, instance=client)
        else:
            return HttpResponseRedirect("/client")

        data = {
            'form': form,
            'client': client,
            'errors': True,
        }
        if form.is_valid():
            data['errors'] = False
            data['client'] = form.save()
            return render(request, 'client-detail.html', data)

        return render(request, 'client-detail.html', data)

    def delete(self, request, **kwargs):
        if 'id' in kwargs:
            client = self._get_client_by_id(request, kwargs['id'])
        else:
            return HttpResponseRedirect("/client")

        # TODO: check if there's any job related to that client

        client.delete()
        return HttpResponseRedirect("/client")

    def post(self, request, **kwargs):
        post = request.POST.copy()
        post['owner'] = request.user.id
        data = {
            'form': ClientForm(post)
        }
        if data['form'].is_valid():
            client = data['form'].save()
            return HttpResponseRedirect("/client/%s" % client.id)

        return render(request, 'client-detail.html', data)
