from django.shortcuts import render
from .forms import ScheduleForm, get_classes
from django.http import HttpResponseRedirect
from dal import autocomplete
import pandas as pd

def calculator(request):
	print(request.method)
	if request.method == 'POST':
		form = ScheduleForm(request.POST)
		print(form)
		if True:
			schedule = {}
			schedule['blockA'] = form.cleaned_data['blockA']
			schedule['blockB'] = form.cleaned_data['blockB']
			schedule['blockC'] = form.cleaned_data['blockC']
			schedule['blockD'] = form.cleaned_data['blockD']
			schedule['blockE'] = form.cleaned_data['blockE']
			schedule['blockF'] = form.cleaned_data['blockF']
			schedule['blockG'] = form.cleaned_data['blockG']
		print("schedule: " + str(schedule))
		return time_display(request, schedule)
	else:
		print('not a post')
		form = ScheduleForm()
		context = {'blocks':['A','B','C'],'form':form}
		return render(request, 'Calculator/index.html', context)

def time_display(request, schedule=None):
	if not schedule:
		context = {'schedule':{'dummy':"dummy_val"},'time':100}
	else:
		new_schedule, total = calc_time(schedule)
		time = to_hrs(total)
		context = {'schedule':new_schedule,'hours':time[0], 'mins':time[1], 'time':total}
		print(context)
	return render(request, 'Calculator/time_display.html', context)

def calc_time(schedule):
	data = pd.read_csv('Calculator/HomeworkSurvey_results_final.xlsx - Sheet1.csv',header=5,names=['Quartile 1','Median','Quartile 3','None','Number of Responses'])
	total = 0
	new_schedule = []
	for block in schedule:
		class_name = schedule[block]
		median_time_spent = data['Median'][class_name]
		new_schedule.append((class_name,median_time_spent))
		total += median_time_spent
		print(block)
	total *= 5/7
	print("sfsdafasdfasdfasdf", new_schedule)
	return new_schedule, total

def to_hrs(time):
	hours = time/60//1
	mins = round(round(time % 1, 2) * 60, 0)
	return [int(hours), int(mins)]


class ClassAutocomplete(autocomplete.Select2ListView):
	def get_list(self):
		return get_classes()
