from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    good = '좋음'
    best = '매우 좋음'
    bad = '나쁨'
    angry = '화남'
    tired = '피곤함'
    MY_FEELING_CHOICES = [
        (good, '좋음'),
        (best, '매우 좋음'),
        (bad, '나쁨'),
        (angry, '화남'),
        (tired, '피곤함'),
    ]
    my_feeling = models.CharField(
        max_length= 5,
        choices= MY_FEELING_CHOICES,
        default = good
    )
    body =models.TextField(default='')