from django.conf.urls import url
from django.views import generic
from dashboard import views

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^client/$', views.ClientView.as_view(), name='client'),
    url(r'^client/(?P<id>[0-9]+)$', views.ClientView.as_view(), name='client'),
    url(r'^service/$', views.ServiceView.as_view(), name='service'),
    url(r'^service/(?P<id>[0-9]+)$', views.ServiceView.as_view(), name='service'),
]
