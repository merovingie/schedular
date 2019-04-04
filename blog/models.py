from django.db import models
from datetime import datetime


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.title}'