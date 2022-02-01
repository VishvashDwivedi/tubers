from statistics import mode
from django.db import models

class Team(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=100, null=True)
    fb_link = models.CharField(max_length=255, null=True)
    insta_link = models.CharField(max_length=255, null=True)
    channel_link = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d/")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " +self.last_name

class Slider(models.Model):
    headline = models.CharField(max_length=255, null=True)
    subtitle = models.CharField(max_length=255, null=True)
    button_text = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to="media/slider/%Y/", default='')
    created_date = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.headline
