from django.db import models
from datetime import datetime


class ResType(models.Model):
    r_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.r_type}"


class Item(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now)
    duration = models.IntegerField(default=1)
    description = models.TextField(default='Insert Description')
    location = models.CharField(max_length=200, blank=True)
    rating = models.IntegerField(default=0)
    comments = models.TextField(blank=True)
    res_type = models.ForeignKey(ResType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} is a , which will take place at {self.location} and it will last {self.duration} hours"



