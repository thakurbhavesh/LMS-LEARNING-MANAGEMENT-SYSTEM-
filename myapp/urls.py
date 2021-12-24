from django.urls import path
from. import views
from django.conf.urls import url

urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("gallery",views.gallery,name='gallery'),
    path("services",views.services,name='services'),
    url(r'^adminlogin',views.adminlogin,name='adminlogin'),
    url(r'^validateadmin',views.validateadmin,name='validateadmin'),
    url(r'^file', views.file, name='file'),

    path('custreg',views.custreg,name='custreg'),
    path('validuser',views.validateuser,name="validateuser"),
    path("register", views.register, name='register'),
]
