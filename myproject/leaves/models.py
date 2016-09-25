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
		return self.get_username()

	def save(self):
		if self.pk is not None:
			super(Employee, self).save()
		else:
			super(Employee, self).save()
			if self.teaching is not True:
				l = LeavesRemain(employee = self, typeofleave = LeaveType.objects.get(name = "Earned"), count = 20)
				l.save()
			if self.permanent is True:
				l = LeavesRemain(employee = self, typeofleave = LeaveType.objects.get(name = "Medical"), count = 20)
				l.save()
			l = LeavesRemain(employee = self, typeofleave = LeaveType.objects.get(name = "Casual"), count = 20)
			l.save()


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
	count 		= models.IntegerField(default=10)


class LeaveRecord(models.Model):
	employee 	= models.ForeignKey(Employee, on_delete = models.CASCADE)
	typeofleave = models.ForeignKey(LeaveType, on_delete = models.CASCADE)
	status		= models.IntegerField()
	reason		= models.CharField(max_length=400, default = "Casual leave")
	date		= models.DateTimeField('leave date')