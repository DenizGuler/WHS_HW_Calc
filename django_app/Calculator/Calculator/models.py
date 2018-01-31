from django.db import models
from django import forms

all_classes = [('Fr2','French 2'), ('Fr3CP','French 3 (CP)'), ('IntroItalian','Intro to Italian Languange and Culture 2')]

class Name(models.Model):
    name = models.CharField(max_length=70, help_text="Name")
    def __str__(self):
    	return self.full_name