from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default="")


class Login(models.Model):
    username=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default="")

class Makerequest(models.Model):
    chname=models.CharField(max_length=50,null=True)
    vhcategory=models.CharField(max_length=50)
    vhnumber=models.CharField(max_length=50)
    vhname=models.CharField(max_length=50)
    vhbrand=models.CharField(max_length=50)    
    vhmodel=models.CharField(max_length=50)
    chphone=models.IntegerField(null=True)
    vhstate=models.CharField(max_length=50)
    vhdistrict=models.CharField(max_length=50)
    vhlocation=models.CharField(max_length=50)
    vhproblem=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default="")
    rqstid=models.IntegerField(null=True)

class Approval(models.Model):
    acost=models.IntegerField()
    adate=models.CharField(max_length=40)
    astatus=models.CharField(max_length=50)
    