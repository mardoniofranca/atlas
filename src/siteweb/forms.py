from django.forms import ModelForm
from .models import Cliente

class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'