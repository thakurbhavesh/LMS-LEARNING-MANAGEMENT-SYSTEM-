from django.shortcuts import render, redirect, reverse
from django.shortcuts import render,redirect
from .models import Complain , Feedback , Course , Notification
from myapp.models import Customer
from datetime import date
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def custhome(r):
    try:
        if r.session['userid']:
            return render(r,'custhome.html')
    except KeyError:
        return render(r,'login.html')

def contact(r):
    return render(r,'contact.html')

def complain(request):
    
    try:
        if request.session['userid']:
            return render(request,'complain.html')
    except KeyError:

            return render(request,'login.html')

def feedback(request):
    try:
        if request.session['userid']:
            return render(request,'feedback.html')
    except KeyError:
            return render(request,'login.html')


def raisecomplain(request):
    complaintext = request.POST['complaintext']
    complaindate = date.today()
    emailaddress = request.session['userid']
    customer = Customer.objects.get(emailaddress=emailaddress)
    name = customer.name
    address = customer.address
    contactno = customer.contactno
    comp = Complain(name=name, address=address, contactno=contactno, emailaddress=emailaddress,
                    complaintext=complaintext, complaindate=complaindate)
    comp.save()
    return redirect('sczone:custhome')


def givefeedback(request):
    feedbacktext = request.POST['feedbacktext']
    feedbackdate = date.today()
    emailaddress = request.session['userid']
    customer = Customer.objects.get(emailaddress=emailaddress)
    name = customer.name
    address = customer.address
    contactno = customer.contactno
    feed = Feedback(name=name, address=address, contactno=contactno, emailaddress=emailaddress,
                    feedbacktext=feedbacktext, feedbackdate=feedbackdate)
    feed.save()
    return redirect('sczone:custhome')
def changepassword(request):
    try:
        if request.session['userid']:
            return render(request,'changepassword.html')
    except KeyError:
            return render(request,'services.html')

def logout(request):
    try:
        if request.session['userid']:
            request.session['userid']=None
            return render(request,'services.html')
    except KeyError:
            return render(request,'register.html')

def changepwd(request):
    oldpassword=request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    emailaddress = request.session['userid']
    msg='Message: '
    if newpassword!=confirmpassword:
        msg=msg+'Newpassword and Confirmpassword are not same'
        return render(request,'changepassword.html',{'msg':msg})
    try:
        customer=Customer.objects.get(emailaddress=emailaddress,password=oldpassword)
        if customer is not None:
            name=customer.name
            gender = customer.gender
            address = customer.address
            age = customer.age
            contactno = customer.contactno
            regdate = customer.regdate
            cust=Customer(name=name,gender=gender,address=address,age=age,contactno=contactno,emailaddress=emailaddress,password=newpassword,regdate=regdate)
            cust.save()
            return redirect('sczone:custhome')

    except ObjectDoesNotExist:
        msg='Oldpassword is not matched'
    return render(request, 'changepassword.html', {'msg': msg})

def course(request):
    pics=Course.objects.all()
    return render(request,'course.html',{"pics":pics})

def notification(request):
    noti=Notification.objects.all()
    return render(request,'notification.html',{"noti":noti})

def checkout(r):
    return render(r,'checkout.html')



