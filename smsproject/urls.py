from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.smsappurls')),
    path('adminapp/',include(('adminapp.adminappurls','adminapp'),namespace='adminapp')),
    path('teacherapp/',include(('teacherapp.teacherappurls','teacherapp'),namespace='teacherapp')),
    path('studentapp/',include(('studentapp.studentappurls','studentapp'),namespace='studentapp')),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)