from django.db import models
from django.urls import reverse # used  in get_absolute_url to get the URL for a specified ID
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

from django.utils import timezone
import uuid

# Create your models here.

# Create your models here.

# class Checking(models.Model):
#     name = models.CharField(max_length=100)
#     check_in = models.DateTimeField(auto_now_add=True)
#     check_out = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return self.na

# model up for review, may not need it

class Client_Waiver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, signed {self.date_time}"
        
    
    def get_absolute_url(self):
        return reverse('client-info', args=[str(self.id)])
    
    

class Feedback_Questions(models.Model):
    question = models.IntegerField(unique=True)
    question_text = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Question {self.question}: {self.question_text}"
    
class Feedback(models.Model):
    feedback_answer = models.CharField(max_length=200)
    # Foreign Keys
    
    feedback_question = models.ForeignKey('Feedback_Questions', on_delete=models.PROTECT, null=True)
    client = models.ForeignKey('Client_Waiver', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"Q{self.feedback_question.question}: {self.feedback_answer}"
    
    
class Waxing_Waiver(models.Model):
    # Questions
    medicine = models.BooleanField(verbose_name="Medicine", default=False) #Field that handles the use of certain medicine
    allergy = models.BooleanField(verbose_name="Bee Allergy", default=False) #Field that handles client allergy to bees
    soap_use = models.BooleanField(verbose_name="Skin Care Use", default= False)
    exposed = models.BooleanField(verbose_name="Light Exposure", default=False)
    health_issues = models.BooleanField(verbose_name="Health Conditions", default=False)
    
    # Other
    timestamp = models.DateTimeField(default=timezone.now)
    agreement = models.CharField(max_length=100) #Client Signature
    client_info = models.ForeignKey('Client_Waiver', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"{self.client_info}, signed {self.timestamp}"


class Services(models.Model):
    service_name = models.CharField(max_length=100)
    selection = models.CharField(max_length=200)
    client_info = models.ForeignKey('Client_Waiver', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.service_name
