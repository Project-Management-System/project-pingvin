from django.http import HttpResponse
from project.models import Project 
from django.shortcuts import render_to_response
from django.template import RequestContext

def newproject(request):
	newpr = Project(name="first pr")
	newpr.save()
	newpr.super_admin.add(request.user)
	return HttpResponse("Hello, world. You're at the poll index.")
def view_pr(request, pr_id):
	c = {}
	c.update({'project':Project.objects.get(pk=pr_id)})
	return render_to_response('projects/project_main.html',c,context_instance=RequestContext(request))
