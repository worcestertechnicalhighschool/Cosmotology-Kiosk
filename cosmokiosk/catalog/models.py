from django.db import models
from django.urls import reverse # used  in get_absolute_url to get the URL for a specified ID
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
import uuid
from django.urls import reverse # used  in get_absolute_url to get the URL for a specified ID
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils import timezone
import uuid

# Create your models here.

# Create your models here.

class Checking(models.Model):
    name = models.CharField(max_length=100)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


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
    client = models.ForeignKey(
        'Client_Waiver', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
        )
    
    def __str__(self):
        return f"Q{self.Feedback_Questions.question}: {self.feedback_answer}"
    
    
class Waxing_Waiver(models.Model):
    answer = models.CharField(max_length=100)
    client = models.ForeignKey(
        'Client Waiver',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    def __str__(self):
        return f"Q{self.client_waiver}"

class Services(models.Model):
    service_name = models.CharField(100)