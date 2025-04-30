from django.shortcuts import render,redirect
from adminapp.models import Teacher,Student,Attendance
from django.core.files.storage import FileSystemStorage
# Create your views here.
def teacherhome(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            return render(req,'teacherhome.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')
    
def teacherprofile(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            if req.method=="POST":
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                address=req.POST['address']
                qualification=req.POST['qualification']
                Teacher.objects.filter(emailaddress=teacherid).update(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,address=address,qualification=qualification)
                return redirect('teacherapp:teacherprofile')
            return render(req,'teacherprofile.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')

def uploadpic(req):
    if req.method=="POST":
        teacherid=req.session['teacherid']
        teacher=Teacher.objects.get(emailaddress=teacherid)
        pic=req.FILES['pic']
        fs=FileSystemStorage()
        filename=fs.save(pic.name,pic)
        teacher.pic=filename
        teacher.save()
        return redirect('teacherapp:teacherprofile')
    
def tchangepass(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            if req.method=="POST":
                oldpassword=req.POST['oldpassword']
                newpassword=req.POST['newpassword']
                cnfpassword=req.POST['cnfpassword']
                if newpassword!=cnfpassword:
                    msg="Please enter same password"
                    return render(req,'tchangepass.html',{'msg':msg})
                elif teacher.password!=oldpassword:
                    msg="Wrong password"
                    return render(req,'tchangepass.html',{'msg':msg})
                elif teacher.password==oldpassword:
                    Teacher.objects.filter(emailaddress=teacherid).update(password=newpassword)
                    return redirect('teacherapp:teacherlogout')
            return render(req,'tchangepass.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')
    
def teacherlogout(req):
    try:
        if req.session['teacherid']!=None:
            del req.session['teacherid']
            return redirect('login')
    except KeyError:
        return redirect('login')
    

def addattend(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            st=Student.objects.filter(sclass=teacher.tclass)
            if req.method=="POST":
                sid=req.POST['sid']
                name=req.POST['name']
                rollno=req.POST['rollno']
                status=req.POST['status']
                created_date=req.POST['created_date']
                att=Attendance(sid=sid,name=name,rollno=rollno,status=status,created_date=created_date)
                att.save()
                return redirect('teacherapp:addattend')
            return render(req,'addattend.html',{'teacher':teacher,'st':st})
    except KeyError:
        return redirect('login')
    
def viewattend(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            return render(req,'viewattend.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')