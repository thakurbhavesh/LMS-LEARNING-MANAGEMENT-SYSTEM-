from django.db import models

# Create your models here.
from django.db.models import TextField

class Customer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    age=models.IntegerField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(primary_key='true')
    password=models.CharField(max_length=20)
    regdate = models.CharField(max_length=20)

class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.caption

class AdminLogin(models.Model):
    adminid = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=20)

class File(models.Model):
    capp=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.capp