from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length=20)

class Employee(models.Model):
	user 		= models.OneToOneField(User, on_delete = models.CASCADE)
	department 	= models.ForeignKey(Department, on_delete = models.CASCADE)
	headofdept 	= models.BooleanField()
	permanent 	= models.BooleanField()
	contact 	= RegexValidator(regex=r'^\+?1?\d{10,12}$', message="Phone number must be of 10 digit length and must be entered in the format: '9999999999'.")

class Leaves(models.Model):
	employee 	= models.ForeignKey(Employee, on_delete = models.CASCADE)
	medical 	= models.IntegerField()
	casual 		= models.IntegerField(default=15)
	earned 		= models.IntegerField()
