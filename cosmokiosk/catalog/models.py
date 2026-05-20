from django.db import models

# Create your models here.

class Checking(models.model):
    name = models.CharField(max_length=100)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name



class Client_Waiver(models.Model):
    First_Name = models.CharField(max_length=200)
