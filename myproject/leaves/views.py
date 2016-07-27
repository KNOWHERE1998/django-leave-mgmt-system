from leaves.forms import EmployeeForm
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Employee

class EmployeeCreate(CreateView):
	model 	= Employee
	fields 	= '__all__'

class EmployeeUpdate(UpdateView):
	model 	= Employee
	fields 	= '__all__'

class EmployeeDelete(DeleteView):
	model 	= Employee
	fields 	= '__all__'
