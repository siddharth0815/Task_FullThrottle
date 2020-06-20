import pytz
from django.db import models
from timezone_field import TimeZoneField
from datetime import datetime


TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class User(models.Model):
	id = models.SlugField(primary_key=True, max_length=200)
	real_name = models.CharField(max_length=50)
	tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

	def __str__(self):
		return self.real_name
   


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    

    
# Create your models here.
