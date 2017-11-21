from django.conf.urls import url
from django.views import generic
from dashboard import views

urlpatterns = [
    url('^$', views.DashboardView.as_view(), name='dashboard'),
]
