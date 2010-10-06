from django.conf.urls.defaults import *

urlpatterns = patterns('ff.project.views',
	(r'newproject','newproject'),
	(r'(?P<pr_id>\d+)/$','view_pr'),
)
