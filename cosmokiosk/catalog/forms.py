from django import forms
from .models import Client_Waiver, Waxing_Waiver, Feedback_Questions, Feedback, Services
from django.core.exceptions import ValidationError
import datetime
from django.utils.translation import gettext_lazy as _



class Client_Waiver(forms.ModelForm):
    class Meta:
        model = Client_Waiver
        fields = ['first_name', 'last_name', 'date_time']

    def clean_date(self):
         date = self.cleaned_data['date_time']

         if date.date() < datetime.date.today():
             raise ValidationError(_('Invalid - date is in the past '))
         
         return date
    
    def clean_first_name(self):
        first_name = self.cleaned_date.get('first_name', '').strip()
        if not first_name:
            raise ValidationError('Name fields cannot be empty.')
        
        for char in first_name:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError('First name can only contain letters.')
            
        return first_name
    
    
    def clean_first_name(self):
        last_name = self.cleaned_date.get('last_name', '').strip()
        if not last_name:
            raise ValidationError('Name fields cannot be empty.')
        
        for char in last_name:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError('Last name can only contain letters.')
            
        return last_name
    
    
    
class Waxing_Waiver(forms.ModelForm):
    class Meta:
        model = Waxing_Waiver
        fields = ['medicine', 'allergy', 'soap_use', 'exposed', 'health_issues', 'timestamp', 'agreement', 'client_info']

    def clean(self):
        cleaned_data = super().clean()
        boolean_fields = ['medicine', 'allergy', 'soap_use', 'exposed', 'health_issues', 'timestamp', 'agreement', 'client_info']
    


        for field in boolean_fields:
            if not cleaned_data.get(field):
                self.add_error(field,_('Please check every box to confirm your waiver agreement'))
        return cleaned_data        