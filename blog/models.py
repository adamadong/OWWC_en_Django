from django.db import models
from django.conf import settings
from django.utils import timezone

class Equipment(models.Model):
    Id_equipment = models.CharField(max_length=100,primary_key=True)
    availability = models.BooleanField()
    capacity = models.CharField(max_length=100)
    pic_url = models.URLField(blank=True)

    def __str__(self):
        return self.Id_equipment
    

class Team(models.Model):
    Country = models.CharField(max_length=100, primary_key=True)
    rank = models.IntegerField()
    state = models.CharField(max_length=20)
    place =models.ForeignKey(Equipment,on_delete=models.CASCADE, related_name='teams')
    flag_url = models.URLField(blank=True)

    def __str__(self):
        return self.Country






# Create your models here.
