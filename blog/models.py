from django.db import models
from django.conf import settings
from django.utils import timezone

class Team(models.Model):
    Country = models.CharField(max_length=100, primary_key=True)
    nb_player = models.CharField(max_length=10)
    rank =models.CharField(max_length=20)

    def __str__(self):
        return self.Country

class Equipment(models.Model):
    Id_equipment = models.CharField(max_length=100,primary_key=True)
    availability = models.BooleanField()
    capacity = models.CharField(max_length=100)

    def __str__(self):
        return self.Id_equipment




# Create your models here.
