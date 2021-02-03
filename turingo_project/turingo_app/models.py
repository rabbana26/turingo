from django.db import models

# Create your models here. 
from django.conf import settings



class Developer(models.Model):
	name = models.CharField(max_length=200,blank=False)
	skillset = models.CharField(max_length=200,blank=False)
	role = models.CharField(max_length=200,blank=False)

	def __str__(self):
		return self.name