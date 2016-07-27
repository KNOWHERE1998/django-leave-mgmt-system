from django.conf.urls import url

from .views import EmployeeCreate, EmployeeUpdate, EmployeeDelete

app_name = 'leaves'

urlpatterns = [
	url(r'employee/add/$', EmployeeCreate.as_view()),
	url(r'employee/(?P<pk>[0-9]+)/$', EmployeeUpdate.as_view()),
	url(r'employee/(?P<pk>[0-9]+)/delete/$', EmployeeDelete.as_view()),
]