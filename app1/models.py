from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=400)
