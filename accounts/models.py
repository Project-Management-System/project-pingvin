from django.db import models
from django.contrib.auth.models import User, UserManager
import datetime

class CustomUser(User):
    birthdate = models.DateField(default=datetime.datetime.now().date())
    country = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    objects = UserManager()
