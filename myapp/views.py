from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from .models import Customer , Image , AdminLogin , File
from datetime import date
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from sczone.models import Notification


def index(request):
    context={"name":" L M S"}
    return render(request,'index.html',context)

def about(request):

    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def register(request):
    return render(request,'register.html')

def gallery(request):
    pics=Image.objects.all()
    return render(request,'gallery.html',{"pics":pics})

def custreg(r):
    password=r.POST['password']
    msg='Message: '
    if len(password)<8:
        msg= msg+'password should be minimum 8 chars'
        return render(r,'register.html',{'msg':msg})
    name = r.POST['name']
    gender = r.POST['gender']
    address = r.POST['address']
    age = r.POST['age']
    contactno = r.POST['contactno']
    emailaddress = r.POST['emailaddress']
    regdate=date.today()
    cust=Customer(name=name,gender=gender,address=address,age=age,contactno=contactno,emailaddress=emailaddress,regdate=regdate,password=password)
    cust.save()
    return redirect('services')
def validateuser(r):
    userid=r.POST['userid']
    password=r.POST['password']
    msg=''
    try:
        user=Customer.objects.get(emailaddress=userid,password=password)
        if user is not None:
            r.session['userid'] = userid
            return redirect(reverse('sczone:custhome'))
    except ObjectDoesNotExist:
        msg=msg+"invalid User"
    return render(r,'services.html',{'msg':msg})

def adminlogin(request):
    nf = Notification.objects.all()
    return render(request,'adminlogin.html',{'nf':nf})

def validateadmin(request):
    adminid=request.POST['adminid']
    password = request.POST['password']
    msg='Message: '
    try:
        admin=AdminLogin.objects.get(adminid=adminid,password=password)
        if admin is not None:
            request.session['adminid']=adminid
            return redirect(reverse('adminzone:adminhome'))
    except ObjectDoesNotExist:
        msg=msg+'Invalid User'
    return render(request,'adminlogin.html',{'msg':msg})

def file(r):
    vids=File.objects.all()
    return render(r,'file.html',{"vids":vids})
