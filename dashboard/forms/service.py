from django.forms import ModelForm
from dashboard.models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['id', 'name', 'base_price', 'owner', ]
