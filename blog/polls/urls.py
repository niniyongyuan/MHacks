from django.conf.urls import patterns, include, url

from polls import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^login/$', views.loginRequest, name='login'),
	url(r'^auth/$', views.auth_view, name='auth'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^loggedin/$', views.loggedin, name='loggedin'),
	url(r'^invalid_login/$', views.invalid_login, name='invalid_login'),
	url(r'^register/$', views.register, name='register'),
	#url(r'^profi/$', views.profile, name='profile'),
	#url(r'^register_success/$', views.register_success, name='register_success'),




    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)