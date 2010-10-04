from django.shortcuts import render_to_response
from django.http import HttpResponse
from project.models import Project 

from django.core.context_processors import csrf

def mainpage(request):
	user = 0
	if request.user.is_authenticated:
		user = request.user
	c = {}
	c.update(csrf(request))
	c.update({'project_list':Project.objects.all().filter(super_admin=user),
			  'user':request.user})
	print user,' ',Project.objects.all().filter(super_admin=user)
	return render_to_response('base.html', c)

