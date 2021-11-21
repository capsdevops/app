from django.forms import ModelForm
from .models import Denuncia


class CreateDenuncia(ModelForm):
    class Meta:
        model = Denuncia
        fields = '__all__'


