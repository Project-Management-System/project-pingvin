from django.db import models
from accounts.models import CustomUser
from datetime import datetime

class Project(models.Model):
    date_started = models.DateField(default=datetime.now())
    name = models.CharField(max_length=100)
    description = models.TextField()
    super_admin = models.ManyToManyField(CustomUser)
    license = models.CharField(max_length=50)
    progess = models.FloatField(default=0)
    web_site = models.URLField()
    def __unicode__(self):
        return self.name

