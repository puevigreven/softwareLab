from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=200)
    expiry_data = models.DateTimeField('date published')
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

class Refill(models.Model):
	 medicine_name = models.CharField(max_length=200)