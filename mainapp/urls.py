from django.conf.urls import url
from .views import *


urlpatterns = [
	url(r'^home/$', home, name='home'),
	url(r'^$', dashboard, name='dashboard'),
	url(r'^area/$', area, name='area'),
	url(r'^water/$', water, name='water'),





]