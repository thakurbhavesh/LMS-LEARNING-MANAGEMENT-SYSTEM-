from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from myapp.models import AdminLogin


# Create your views here.
from sczone.models import Feedback,Complain

from myapp.models import Customer

from sczone.models import Notification

from myapp.models import Image


def adminhome(request):
    try:
        if request.session['adminid']:
            feed=Feedback.objects.all()
            return render(request,'adminhome.html',{'feed':feed})
    except KeyError:
        return render(request, 'adminlogin.html')

def deletefeedback(request,id):
    f=Feedback.objects.get(id=id)
    f.delete()
    return redirect('adminzone:adminhome')

def customer(request):
    try:
        if request.session['adminid']:
            cust=Customer.objects.all()
            return render(request,'customer.html',{'cust':cust})
    except KeyError:
        return render(request, 'adminlogin.html')

def deletecustomer(request,eid):
    cust=Customer.objects.get(emailaddress=eid)
    cust.delete()
    return redirect('adminzone:customer')

def acomplain(request):
    try:
        if request.session['adminid']:
            comp=Complain.objects.all()
            return render(request,'acomplain.html',{'comp':comp})
    except KeyError:
        return render(request, 'adminlogin.html')

def deletecomplain(request,id):
    c=Complain.objects.get(id=id)
    c.delete()
    return redirect('adminzone:adminhome')

def adminchangepwd(request):
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']

    msg = 'Message: '
    if newpassword != confirmpassword:
        msg = msg + 'Newpassword and Confirmpassword are not matched'
        return render(request, 'achangepassword.html', {'msg': msg})
    adminid=request.session['adminid']
    try:
        admin=AdminLogin.objects.get(adminid=adminid,password=oldpassword)
        if admin is not None:
            ad=AdminLogin(adminid=adminid,password=newpassword)
            ad.save()
            return redirect('adminzone:logout')
    except ObjectDoesNotExist:
        msg=msg+"Oldpassword is not matched"
    return render(request,'achangepassword.html',{'msg':msg})

def achangepassword(request):
    try:
        if request.session['adminid']:
            return render(request,'achangepassword.html')
    except KeyError:
        return render(request, 'adminlogin.html')

def logout(request):
    try:
        if request.session['adminid']:
            request.session['adminid']=None
            return render(request,'adminlogin.html')
    except KeyError:
        return render(request, 'adminlogin.html')

def addnotification(request):
    text=request.POST['text']
    date=request.POST['date']
    nf=Notification(text=text,date=date)
    nf.save()
    return redirect('adminzone:adminhome')

def deletenotification(request,id):
    n=Notification.objects.get(id=id)
    n.delete()
    return redirect('adminzone:adminhome')

def anotification(request):
    try:
        if request.session['adminid']:
            nf=Notification.objects.all()
            return render(request,'anotification.html',{'nf':nf})
    except KeyError:
        return render(request, 'adminlogin.html')

