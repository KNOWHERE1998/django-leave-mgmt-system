from __future__ import unicode_literals
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Employee(User):
	department 	= models.ForeignKey('leaves.Department', on_delete = models.CASCADE)
	headofdept 	= models.BooleanField()
	permanent 	= models.BooleanField()
	teaching	= models.BooleanField()
	contact 	= PhoneNumberField(help_text="Please use the following format: <em>+91__________</em>.")

	def __str__(self):
		return self.user.get_username()



class Department(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name

class LeaveType(models.Model):
	name = models.CharField(max_length=20, default = "somevalue")
	def __str__(self):
		return self.name

class LeavesRemain(models.Model):
	employee	= models.ManyToManyField(Employee)
	typeofleave = models.ManyToManyField(LeaveType)
	def __str__(self):
		return self.name

class LeaveRecord(models.Model):
	employee 	= models.ForeignKey(Employee, on_delete = models.CASCADE)
	typeofleave = models.ForeignKey(LeaveType, on_delete = models.CASCADE)
	status		= models.IntegerField()
	reason		= models.CharField(max_length=400, default = "Casual leave")
	date		= models.DateTimeField('leave date')