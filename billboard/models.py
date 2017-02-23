from django.db import models
from django.utils import timezone

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=400)
    author = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

