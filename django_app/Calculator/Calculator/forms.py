from django import forms
from .models import Name
from dal import autocomplete
import pandas as pd

data = pd.read_csv('Calculator/HomeworkSurvey_results_final.xlsx - Sheet1.csv',header=5,names=['Quartile 1','Median','Quartile 3','None','Number of Responses'])
all_classes = [(x,x) for x in list(data.index)]
classes = list(data.index)

def get_classes():
	return list(data.index)

#all_classes = [('French 2','French 2'), ('French 3 (CP)','French 3 (CP)'), ('Intro to Italian Languange and Culture 2','Intro to Italian Languange and Culture 2')]
class ScheduleForm(forms.ModelForm):
	#blockA = autocomplete.ListSelect2(url='class-autocomplete')
	blockA = autocomplete.Select2ListChoiceField(
        choice_list=get_classes,
        widget=autocomplete.ListSelect2(url='class-autocomplete'),
		help_text="A Block"
    )
	#testA = forms.ModelChoiceField(queryset=all_classes, widget=autocomplete.ModelSelect2(url='classes-autocomplete'))
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
