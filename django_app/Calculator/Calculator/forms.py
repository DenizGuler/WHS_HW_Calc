from django import forms
from .models import Name
import pandas as pd

data = pd.read_csv('Calculator/HomeworkSurvey_results_final.xlsx - Sheet1.csv',header=5,names=['Quartile 1','Median','Quartile 3','None','Number of Responses'])
all_classes = [(x,x) for x in list(data.index)]
#all_classes = [('French 2','French 2'), ('French 3 (CP)','French 3 (CP)'), ('Intro to Italian Languange and Culture 2','Intro to Italian Languange and Culture 2')]
class ScheduleForm(forms.ModelForm):
	blockA = forms.ChoiceField(choices=all_classes, help_text="A Block")
	blockB = forms.ChoiceField(choices=all_classes, help_text="B Block")
	blockC = forms.ChoiceField(choices=all_classes, help_text="C Block")
	blockD = forms.ChoiceField(choices=all_classes, help_text="D Block")
	blockE = forms.ChoiceField(choices=all_classes, help_text="E Block")
	blockF = forms.ChoiceField(choices=all_classes, help_text="F Block")
	blockG = forms.ChoiceField(choices=all_classes, help_text="G Block")
	class Meta:
		model = Name
		exclude = ()

class Schedule2Form(forms.Form):
	my_blocks = forms.ChoiceField(choices=[('Fr2','French 2'), ('Fr3CP','French 3 (CP)'), ('IntroItalian','Intro to Italian Languange and Culture 2')])