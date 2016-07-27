from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user']}),
        ('Department', {'fields': ['department', 'headofdept']}),
        ('Miscellenous', {'fields': ['permanent',]})
    ]
    

admin.site.register(Employee, EmployeeAdmin)