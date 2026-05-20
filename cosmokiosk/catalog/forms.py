from django import forms
from .models import Checking


class CheckingForm(forms.ModelForm):
    class Meta:
        model = Checking
        fields = ['name']