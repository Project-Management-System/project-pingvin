from django.http import HttpResponse
from project.models import Project 

def newproject(request):
	newpr = Project(name="first pr")
	newpr.save()
	newpr.super_admin.add(request.user)
	return HttpResponse("Hello, world. You're at the poll index.")
