from django.db import models
# Create your models here.


class Room(models.Model):
    Name = models.CharField(max_length=20,null=True)
    Age = models.CharField(max_length=20,null=True)