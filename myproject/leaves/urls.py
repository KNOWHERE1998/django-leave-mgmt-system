from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from .views import *
from django.conf.urls import url, include

app_name = 'leaves'

urlpatterns = patterns('',
	url(r'^home/$', home),
	url(r'^profile/$', home),
	url(r'^$', RedirectView.as_view(url='/')),
	url(r'^logout/$', 'django.contrib.auth.views.logout'), 
	url(r'^login/$', 'django.contrib.auth.views.login'), 
	url(r'^$', 'django.contrib.auth.views.login'),
	url(r'^$', 'django.contrib.auth.views.login'),
)