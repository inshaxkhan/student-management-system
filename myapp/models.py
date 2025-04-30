from django.db import models

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    query=models.TextField()
    querydate=models.CharField(max_length=30)

class AdminLogin(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
