from django.shortcuts import render
from .forms import ScheduleForm
from django.http import HttpResponseRedirect


def calculator(request):
	if request.method == 'POST':
		form = ScheduleForm(request.POST)
		if True:
			schedule = {}
			schedule['blockA'] = form.cleaned_data['blockA']
			schedule['blockB'] = form.cleaned_data['blockB']
			schedule['blockC'] = form.cleaned_data['blockC']
			schedule['blockD'] = form.cleaned_data['blockD']
			schedule['blockE'] = form.cleaned_data['blockE']
			schedule['blockF'] = form.cleaned_data['blockF']
			schedule['blockG'] = form.cleaned_data['blockG']
		print("schedule: " + schedule)
		return time_display(request, schedule)
	else:
		print('uhh')
		form = ScheduleForm()
		context = {'blocks':['A','B','C'],'form':form}
		return render(request, 'Calculator/index.html', context)

def time_display(request, schedule=None):
	if not schedule:
		context = {'schedule':{'dummy':"dummy_val"},'time':100}
	else:
		context = {'schedule':schedule,'time':calc_time(schedule)}
	return render(request, 'Calculator/time_display.html', context)

def calc_time(schedule):
	#do some calculations here
	return 100