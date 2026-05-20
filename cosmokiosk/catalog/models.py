from django.db import models

# Create your models here.
class Client_Waiver(models.Model):
    First_Name = models.CharField(max_length=200)
