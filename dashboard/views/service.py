from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from dashboard.forms import ServiceForm
from dashboard.models import Service


class ServiceView(LoginRequiredMixin, ListView):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'patch':
            return self.patch(*args, **kwargs)
        elif method == 'delete':
            return self.delete(*args, **kwargs)
        return super(ServiceView, self).dispatch(*args, **kwargs)

    def _get_service_by_id(self, request, _id):
        try:
            service = Service.objects.get(id=_id)
        except Service.DoesNotExist:
            return HttpResponseRedirect('/dashboard/service')
        else:
            if service.owner != request.user:
                return HttpResponseRedirect('/dashboard/service')
        return service

    def get(self, request, **kwargs):
        data = {}
        if 'id' in kwargs:
            data = {
                'form': ServiceForm(),
            }
            if kwargs['id'] != '0':
                service = self._get_service_by_id(request, kwargs['id'])
                data['form'] = ServiceForm(instance=service)
                data['service'] = service
            return render(request, 'service-detail.html', data)
        else:
            data['services'] = Service.objects.filter(owner=request.user)
            return render(request, 'service-list.html', data)

    def patch(self, request, **kwargs):
        if 'id' in kwargs:
            service = self._get_service_by_id(request, kwargs['id'])
            post = request.POST.copy()
            post['owner'] = request.user.id
            form = ServiceForm(post, instance=service)
        else:
            return HttpResponseRedirect("/service")

        data = {
            'form': form,
            'service': service,
            'errors': True,
        }
        if form.is_valid():
            data['errors'] = False
            data['service'] = form.save()
            return render(request, 'service-detail.html', data)

        return render(request, 'service-detail.html', data)

    def delete(self, request, **kwargs):
        if 'id' in kwargs:
            service = self._get_service_by_id(request, kwargs['id'])
        else:
            return HttpResponseRedirect("/service")

        service.delete()
        return HttpResponseRedirect("/service")

    def post(self, request, **kwargs):
        post = request.POST.copy()
        post['owner'] = request.user.id
        data = {
            'form': ServiceForm(post)
        }
        if data['form'].is_valid():
            service = data['form'].save()
            return HttpResponseRedirect("/service/%s" % service.id)

        return render(request, 'service-detail.html', data)
