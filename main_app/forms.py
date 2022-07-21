from django.forms import ModelForm
from .models import Trim

class TrimForm(ModelForm):
    class Meta:
        model = Trim
        fields = ['name', 'price_inc']