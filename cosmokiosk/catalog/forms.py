from django import forms
from .models import Client_Waiver, Waxing_Waiver, Feedback_Questions, Feedback, Services
from django.core.exceptions import ValidationError

class ClientWaiverForm(forms.ModelForm):
    class Meta:
        model = Client_Waiver
        fields = set([field.name for field in Client_Waiver._meta.fields if field.name != 'id'])        
    