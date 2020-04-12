from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^mainpage/$', views.index, name='mainpage'),
	url(r'^register/$', views.register, name='register'),
	url(r'^about/$', views.about, name='about'),
	url(r'^whatsapp/$', views.whatsapp_redirect, name='whatsapp'),

]
