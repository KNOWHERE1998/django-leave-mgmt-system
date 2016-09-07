from django.contrib import admin
from .models import LeaveRecord, Employee
from django import forms
from django.forms import ModelForm, PasswordInput

class EmployeeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Login Information', 	{'fields': ['username', 'password']}),
		('Account Information', {'fields': ['first_name', 'last_name', 'email']}),
		('Department', 			{'fields': ['department', 'headofdept']}),
		('Miscellenous', 		{'fields': ['permanent', 'teaching', 'contact']})
	]

admin.site.register(Employee, EmployeeAdmin)


admin.site.register(LeaveRecord)