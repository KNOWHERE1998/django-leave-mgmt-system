from __future__ import unicode_literals
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class Employee(models.Model):
	user 		= models.OneToOneField(User, on_delete = models.CASCADE)
	department 	= models.ForeignKey(Department, on_delete = models.CASCADE)
	headofdept 	= models.BooleanField()
	permanent 	= models.BooleanField()
	contact 	= PhoneNumberField()

class LeaveType(models.Model):
	name = models.CharField(max_length=20, default = "somevalue")
	
class LeavesRemain(models.Model):
	employee	= models.ManyToManyField(Employee)
	typeofleave = models.ManyToManyField(LeaveType)
	def __str__(self):
		return self.name
class LeaveRecord(models.Model):
	employee 	= models.ForeignKey(Employee, on_delete = models.CASCADE)
	typeofleave = models.ForeignKey(LeaveType, on_delete = models.CASCADE)
	date		= models.DateTimeField('leave date')