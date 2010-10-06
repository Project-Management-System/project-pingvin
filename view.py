from django.shortcuts import render_to_response
from django.http import HttpResponse
from project.models import Project 

from django.core.context_processors import csrf

def mainpage(request):
	c = {}
	c.update(csrf(request))
	if request.user.is_authenticated():
		c.update({'project_list':Project.objects.all().filter(super_admin=request.user),'user':request.user})
	return render_to_response('base.html', c)

