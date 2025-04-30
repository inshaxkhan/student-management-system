from django.urls import path
from . import views
urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('viewenquiry/',views.viewenquiry,name='viewenquiry'),
    path('addclass/',views.addclass,name='addclass'),
    path('viewclass/',views.viewclass,name='viewclass'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('addsubject/',views.addsubject,name='addsubject'),
    path('viewsubject/',views.viewsubject,name='viewsubject'),
    path('delenq/<id>',views.delenq,name='delenq'),
    path('delsubject/<sid>',views.delsubject,name='delsubject'),
    path('delclass/<cid>',views.delclass,name='delclass'),
    path('delteacher/<id>',views.delteacher,name='delteacher'),
    path('editclass/<id>',views.editclass,name='editclass'),
    path('editteacher/<id>',views.editteacher,name='editteacher'),
    path('addteacher/',views.addteacher,name='addteacher'),
    path('viewteacher/',views.viewteacher,name='viewteacher'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
]