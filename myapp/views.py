from django.shortcuts import render, redirect
from . models import Enquiry, AdminLogin
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from adminapp.models import Teacher,Student

def index(req):
    return render(req, "index.html")

def contactus(req):
    if req.method=="POST":
        name=req.POST['name']
        email=req.POST['email']
        phone=req.POST['phone']
        query=req.POST['query']
        querydate=timezone.now()

        enq=Enquiry(name=name, email=email, phone=phone, query=query, querydate=querydate)
        enq.save()
        msg="Your enquiry is submitted successfully!"
        return render(req,'contactus.html',{'msg':msg})
    
    return render(req, 'contactus.html')

def login(req):
    return render(req, 'login.html')

def loguser(req):
    if req.method=="POST":
        usertype=req.POST['usertype']
        userid=req.POST['userid']
        password=req.POST['password']

        if usertype=="admin":
            try:
                user=AdminLogin.objects.get(userid=userid,password=password)
                if user is not None:
                    req.session['adminid']=userid
                    return redirect('adminapp:adminhome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})
            
        elif usertype=="teacher":
            try:
                teacher=Teacher.objects.get(emailaddress=userid,password=password)
                if teacher is not None:
                    req.session['teacherid']=userid
                    return redirect('teacherapp:teacherhome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})
            
        elif usertype=="student":
            try:
                student=Student.objects.get(emailaddress=userid,password=password)
                if student is not None:
                    req.session['studentid']=userid
                    return redirect('studentapp:studenthome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})