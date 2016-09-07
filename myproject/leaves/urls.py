from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from .views import *
from django.conf.urls import patterns, url, include
from django.contrib.auth.views import password_reset, password_reset_done

app_name = 'leaves'

urlpatterns = patterns('',
	url(r'^profile/$', home),
	url(r'^$', RedirectView.as_view(url='/')),
	url(r'^logout/$', 'django.contrib.auth.views.logout'), 
	url(r'^login/$', 'django.contrib.auth.views.login'), 
	url(r'^$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', logout_page),
	url(r'^home/$', home),
	url(r'^password/reset/$', password_reset, {'template_name': 'my_templates/password_reset.html'}),
)
