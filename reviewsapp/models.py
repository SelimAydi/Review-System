from django.db import models
import datetime

# Create your models here.

class Reviews(models.Model):
	user_name = models.CharField(max_length=30, blank=True, null=True)
	rating = models.IntegerField()
	review = models.CharField(max_length=1000)
	date = models.DateField(auto_now_add=True)