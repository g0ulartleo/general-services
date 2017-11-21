from django.conf.urls import url
from django.views import generic
from dashboard import views

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'clients/$', views.ClientView.as_view(), name='clients'),
]
