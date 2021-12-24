from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^adminhome', views.adminhome, name='adminhome'),
url(r'^customer', views.customer, name='customer'),
url(r'^acomplain', views.acomplain, name='acomplain'),
url(r'^anotification', views.anotification, name='anotification'),

url(r'^deletecomplain/(?P<id>\d+)$', views.deletecomplain, name='deletecomplain'),
url(r'^deletefeedback/(?P<id>\d+)$', views.deletefeedback, name='deletefeedback'),
url(r'^achangepassword', views.achangepassword, name='achangepassword'),
url(r'^adminchangepwd', views.adminchangepwd, name='adminchangepwd'),
url(r'^logout', views.logout, name='logout'),
url(r'^addnotification', views.addnotification, name='addnotification'),
url(r'^deletenotification/(?P<id>\d+)$', views.deletenotification, name='deletenotification'),

]