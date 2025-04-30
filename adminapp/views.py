from django.shortcuts import render,redirect
from myapp.models import Enquiry
from django.utils import timezone
from . models import *
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def adminhome(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            return render(req,'adminhome.html',{'adminid':adminid})
    except KeyError:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def viewenquiry(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            enq=Enquiry.objects.all()
            return render(req,'viewenquiry.html',{'adminid':adminid,'enq':enq})
    except KeyError:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def addclass(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            if req.method=="POST":
                class_name=req.POST['class_name']
                seats=req.POST['seats']
                roomno=req.POST['roomno']
                created_date=timezone.now()
                cl=Classes(class_name=class_name,seats=seats,roomno=roomno,created_date=created_date)
                cl.save()
                return redirect('adminapp:viewclass')
            return render(req,'addclass.html',{'adminid':adminid})
    except KeyError:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)   
def viewclass(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            return render(req,'viewclass.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def adminlogout(req):
    try:
        if req.session['adminid']!=None:
            del req.session['adminid']
            return redirect('login')
    except KeyError:
        return redirect('login')
    
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def addsubject(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            # adding subject details into database
            if req.method=="POST":
                subject_name=req.POST['subject_name']
                sclass=req.POST['sclass']
                book=req.POST['book']
                steacher=req.POST['steacher']
                created_date=timezone.now()
                addSub=Subject(subject_name=subject_name,sclass=sclass,book=book, steacher=steacher, created_date=created_date)
                addSub.save()
                return redirect('adminapp:viewsubject') 
            
            return render(req,'addsubject.html',{'adminid':adminid})
    except KeyError:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def viewsubject(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            subj=Subject.objects.all()
            return render(req,'viewsubject.html',{'adminid':adminid, 'subj':subj})
    except KeyError:
        return redirect('login')
    
def delenq(req,id):
    try:
        if req.session['adminid']!=None:
            Enquiry.objects.get(id=id).delete()
            return redirect('adminapp:viewenquiry')
    except KeyError:
        return redirect('login')
    
def editclass(req,id):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.get(cid=id)
            if req.method == 'POST':
                class_name=req.POST['class_name']
                seats=req.POST['seats']
                roomno=req.POST['roomno']
                Classes.objects.filter(cid=id).update(class_name=class_name,seats=seats,roomno=roomno)
                return redirect('adminapp:viewclass')
            return render(req,'editclass.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login')          


def addteacher(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            if req.method=="POST":
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                emailaddress=req.POST['emailaddress']
                tclass=req.POST['tclass']
                address=req.POST['address']
                salary=req.POST['salary']
                qualification=req.POST['qualification']
                created_date=timezone.now()
                tech=Teacher(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,tclass=tclass,address=address,salary=salary,qualification=qualification,created_date=created_date,password="12345")
                tech.save()
                return redirect('adminapp:viewteacher')
            return render(req,'addteacher.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login')   


def viewteacher(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            tech=Teacher.objects.all()
            return render(req,'viewteacher.html',{'adminid':adminid,'tech':tech})
    except KeyError:
        return redirect('login') 

def delclass(req,cid):
    try:
        if req.session!=None:
            Classes.objects.get(cid=cid).delete()
            return redirect('adminapp:viewclass')    
    except KeyError:
        return redirect('login')         

def delsubject(req,sid):
    try:
        if req.session!=None:
            Subject.objects.get(sid=sid).delete()
            return redirect('adminapp:viewsubject')    
    except KeyError:
        return redirect('login')    
        

def delteacher(req,id):
    try:
        if req.session!=None:
            Teacher.objects.get(id=id).delete()
            return redirect('adminapp:viewteacher')    
    except KeyError:
        return redirect('login')    
            
def editteacher(req,id):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            tech=Teacher.objects.get(id=id)
            if req.method == 'POST':
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                emailaddress=req.POST['emailaddress']
                tclass=req.POST['tclass']
                address=req.POST['address']
                salary=req.POST['salary']
                qualification=req.POST['qualification']
                Teacher.objects.filter(id=id).update(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,tclass=tclass,address=address,salary=salary,qualification=qualification)
                return redirect('adminapp:viewteacher')
            return render(req,'editteacher.html',{'adminid':adminid,'tech':tech})
    except KeyError:
        return redirect('login')
    
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def addstudent(req):
    # try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            if req.method=="POST":
                rollno=req.POST['rollno']
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                emailaddress=req.POST['emailaddress']
                sclass=req.POST['sclass']
                address=req.POST['address']
                feespaid=req.POST['feespaid']
                duefees=req.POST['duefees']
                created_date=timezone.now()
                password="12345"
                st=Student(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,sclass=sclass,address=address,feespaid=feespaid,duefees=duefees,password=password,created_date=created_date)
                st.save()
                return redirect('adminapp:viewstudent')
            return render(req,'addstudent.html',{'adminid':adminid,'cl':cl})
    # except KeyError:
    #     return redirect('login')
    
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def viewstudent(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            stud=Student.objects.all()
            return render(req,'viewstudent.html',{'adminid':adminid,'stud':stud})
    except KeyError:
        return redirect('login')
    

def delstudent(req,id):
    try:
        if req.session!=None:
            Student.objects.get(id=id).delete()
            return redirect('adminapp:viewstudent')    
    except KeyError:
        return redirect('login')    
            
def editstudent(req,id):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            stud=Student.objects.get(id=id)
            if req.method == 'POST':
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                emailaddress=req.POST['emailaddress']
                address=req.POST['address']
                sclass=req.POST['sclass']
                paidfees=req.POST['paidfees']
                duefees=req.POST['duefees']
                password=req.POST['password']
                pic=req.POST['pic']
                created_date=req.POST['created_date']
                Student.objects.filter(id=id).update(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,emailaddress=emailaddress,address=address,sclass=sclass,paidfees=paidfees,duefees=duefees,password=password,pic=pic,created_date=created_date)
                return redirect('adminapp:viewstudent')
            return render(req,'editstudent.html',{'adminid':adminid,'stud':stud})
    except KeyError:
        return redirect('login')