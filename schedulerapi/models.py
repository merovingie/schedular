from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from django.utils import timezone

MY_CHOICES = (('HIGH', 'HIGH'),
              ('MEDIUM', 'MEDIUM'),
              ('LOW', 'LOW'))

class Item(models.Model):
    severity = models.CharField(choices=MY_CHOICES, max_length=128)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=300)
    monthly = models.BooleanField(default=False)
    weekly = models.BooleanField(default=False)
    daily = models.BooleanField(default=False)
    yearly = models.BooleanField(default=False)
    priorty = models.IntegerField(default= 0)
    timeNow = models.DateTimeField(auto_now_add=True)
    timeScheduled = models.DateTimeField()

    def __str__(self):
        return  self.title

class Pick(models.Model):
    dayDate = models.DateTimeField(auto_now_add=True)
    itemA = models.CharField(max_length=32)
    isDoneA = models.BooleanField(default=False)
    itemB = models.CharField(max_length=32)
    isDoneB = models.BooleanField(default=False)
    itemC = models.CharField(max_length=32)
    isDoneC = models.BooleanField(default=False)

    def __str__(self):
        return  str(self.dayDate)
