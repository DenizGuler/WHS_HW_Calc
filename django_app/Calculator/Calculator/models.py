from django.db import models
from django import forms

all_classes = [('French 2','French 2'), ('French 3 (CP)','French 3 (CP)'), ('Intro to Italian Languange and Culture 2','Intro to Italian Languange and Culture 2')]

class Name(models.Model):
    name = models.CharField(max_length=70, help_text="Name")
    def __str__(self):
    	return self.full_name