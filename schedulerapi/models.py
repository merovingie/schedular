from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from django.utils import timezone

class Item(models.Model):
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

