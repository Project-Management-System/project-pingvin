from django.conf.urls.defaults import *
from registration.forms import RegistrationFormUniqueEmail
from project.models import Project

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^admin/', include(admin.site.urls)),
     
     url(r'^account/register/', 'registration.views.register', {'form_class': RegistrationFormUniqueEmail}, name='registration_register'),
     (r'^account/', include('registration.urls')),
     (r'^projects/', include('project.urls')),
     url(r'^$', 'view.mainpage'),

)
