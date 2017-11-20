from django.conf.urls import url
from django.views import generic
from services import views

urlpatterns = [
    url('^$', views.DashboardView.as_view(), name='dashboard'),
]
