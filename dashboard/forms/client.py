from django.forms import ModelForm
from dashboard.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'cpf', 'primary_phone_number',
                  'secondary_phone_number', 'address', 'owner', ]
