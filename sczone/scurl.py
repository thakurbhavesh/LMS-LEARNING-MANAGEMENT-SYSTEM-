from django.conf.urls import url
from django.urls import path
from. import views

urlpatterns = [
    url(r'^custhome', views.custhome, name='custhome'),
    url(r'^complain', views.complain, name='complain'),
    url(r'^feedback', views.feedback, name='feedback'),
    url(r'^raisecomplain', views.raisecomplain, name='raisecomplain'),
    url(r'^givefeedback', views.givefeedback, name='givefeedback'),
    url(r'^changepwd', views.changepwd, name='changepwd'),
    url(r'^changepassword', views.changepassword, name='changepassword'),
    url(r'^course', views.course, name='course'),
    url(r'^notification', views.notification, name='notification'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^checkout', views.checkout, name='checkout'),



]