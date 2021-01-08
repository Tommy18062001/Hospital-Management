from django.db import models

# Create your models here.


class Account(models.Model):
    date = models.DateTimeField()
    User_name = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    content = models.TextField()