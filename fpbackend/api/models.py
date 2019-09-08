from django.db import models

class Place(models.Model):
	name = models.CharField(max_length=100)
	link = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
