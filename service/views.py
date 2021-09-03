# from django.http.response import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse, request
from service.models import *
from django.core.mail import send_mail
# Create your views here.
def home(request):
    msg=""
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data={
            'name':name,
            'mail':email,
            'subject':subject,
            'message':message,
        }
        message = ''''
        New message:{}
        From:{}
        '''.format(data['message'],data['mail'])
        send_mail(data['subject'],message,'',['surabhic09@gmail.com'])
        print('sent')
        msg="Message Sent"
    
    return render(request,"index.html",{'msg':msg})

def signup(request):
    msg=""
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('psw')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            if Registration.objects.filter(name=name):
                msg="username already exist"
                return render(request,"signup.html",{'msg':msg}) 
            else:
                if Registration.objects.filter(password=password):
                    msg="password already exist"
                    return render(request,"signup.html",{'msg':msg})
                else:
                    data=Registration.objects.create(name=name,email=email,password=password,status=1)
                    data=Login.objects.create(username=name,password2=password,status=1)
                    msg="Registration successfully done!!!"
                    return render(request,"login.html",{'msg':msg})
        else:
            msg="Password not match...!!!"
    return render(request,"signup.html",{'msg':msg})

def login(request):
    msg=""
    if request.method=='POST':
        username=request.POST.get('cname')
        password2=request.POST.get('cpass')
        if Login.objects.filter(username=username,password2=password2):
            data=Registration.objects.get(name=username,password=password2)
            request.session['userid']=data.id
            if data.status=='admin':
                return render(request,"adminsec.html",{'msg':msg})
            elif data.status=='1':
                return render(request,"request.html",{'msg':msg})
        else:
            msg="incorrect username or password"
    return render(request,"login.html",{'msg':msg})

def requests(request):
    return render(request,"request.html") 

def makerequest(request):
    if request.session['userid']:
        uid=request.session['userid']
    msg=""
    if request.method=='POST':
        cname=request.POST.get('cname')
        vcat=request.POST.get('vcat')
        vnumber=request.POST.get('vnumber')
        vname=request.POST.get('vname')
        vbrand=request.POST.get('vbrand')
        vmodel=request.POST.get('vmodel')
        vphone=request.POST.get('vphone')
        vstate=request.POST.get('vstate')
        vdistrict=request.POST.get('vdistrict')
        vlocation=request.POST.get('vloc')
        vproblem=request.POST.get('vproblem')

        data=Makerequest.objects.create(chname=cname,vhcategory=vcat,vhnumber=vnumber,vhname=vname,vhbrand=vbrand,vhmodel=vmodel,chphone=vphone,vhstate=vstate,vhdistrict=vdistrict,vhlocation=vlocation,vhproblem=vproblem,rqstid=uid,status=1)    
    return render(request,"make_rqst.html")

def aprvdrequest(request):
    if request.session['userid']:
        uid=request.session['userid']
    data=Makerequest.objects.filter(rqstid=uid)
    return render(request,"aprvd_rqst.html",{'data':data})

def bill(request):
    if request.session['userid']:
        uid=request.session['userid']
    data=Makerequest.objects.filter(rqstid=uid)
    data2=Approval.objects.all()
    return render(request,"rqstbill.html",{'data':data,'data2':data2})

def alogin(request):
    msg=""
    if request.method=='POST':
        username=request.POST.get('aname')
        password2=request.POST.get('apass')
        if Login.objects.filter(username=username,password2=password2):
            data=Registration.objects.get(name=username,password=password2)
            request.session['userid']=data.id
            if data.status=='admin':
                data=Makerequest.objects.all()
                print(data)
                return render(request,"adminsec.html",{'data':data})
            elif data.status=='1':
                return render(request,"request.html",{'msg':msg})
        else:
            msg="incorrect username or password"

    return render(request,'adminlogin.html')

def approve(request):
    msg=""
    if request.method=='POST':
        cost=request.POST.get('cost')
        date=request.POST.get('date')
        pstatus=request.POST.get('status')
        data2=Approval.objects.create(acost=cost,adate=date,astatus=pstatus)
        
    return render(request,"approval.html") 

  

          