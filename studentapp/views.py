from django.shortcuts import render,redirect
from adminapp.models import Student
# Create your views
def studenthome(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            return render(req,'studenthome.html',{'student':student})
    except KeyError:
        return redirect('login')