from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage' : 'I am the bold message from the context!'}
	return render_to_response('rango/index.jade', context_dict, context)

def about(request):
	return HttpResponse('Rango says "Here is the About page". ' +
		'<a href="/rango">Index</a>')


