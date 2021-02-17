from django.db import models

class Profile(models.Model):
	name = models.CharField(max_length=100)
	age = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add=True)
