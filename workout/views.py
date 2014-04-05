from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from workout.models import ExerciseEvent

def index(request):
	latest_poll_list = ExerciseEvent.objects.order_by('-startTime')[:5]
	template = loader.get_template('workout/index.html')
	context = RequestContext(request, {'latest_poll_list': latest_poll_list})
	return HttpResponse(template.render(context))
def detail(request, poll_id):
	try:
		poll = ExerciseEvent.objects.get(pk=poll_id)
	except ExerciseEvent.DoesNotExist:
		raise Http404
	return render(request, 'workout/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

def makeEvent(request):
	return render(request, 'workout/applejack.html')