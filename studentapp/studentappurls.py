from django.urls import path
from . import views

urlpatterns=[
    path('studentapp/',views.studenthome,name='studenthome'),
]