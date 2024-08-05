from django.http import HttpResponse
from django.shortcuts import render

from service.models import login1
from service.models import hospital_profile
from service.models import hospital
from service.models import profilepatient
from service.models import appointment
from service.models import doctor

from django.core.mail import send_mail
from django.db import connection
from Hospital_Management_System import view as vp
import random
from datetime import datetime
from datetime import time
from datetime import date

import time



OTP = 0
log=""
pro=""
def index(request):
    return render(request,"home.html")

def signinn(request):
    return render(request,"signin.html")

def signin(request):
    n=""
    if request.method=="POST":
        emailid=request.POST.get('emailid')
        password=request.POST.get('password')
        print(emailid)
        pas = login1.objects.raw("select id,password from service_login1 where email= %s", [emailid])
        p = hospital_profile.objects.raw("select id,P_H_password from service_hospital_profile where  p_H_email= %s", [emailid])
        if len(pas)>0:
            if password==pas[0].password:
               
               a = login1.objects.raw("select * from service_login1 where email = %s",[emailid])
               b = profilepatient.objects.raw("select * from service_profilepatient where email = %s",[emailid])
               if (b[0].bloodgroup == None) or (b[0].phone == None) or (b[0].dateofbirth == None) or (b[0].address == None):
                    request.session['ss']=emailid
                    n="please fill all the profile details"
                    if 'ss' in request.session:
                        return render(request,"indexpatient.html",{'n':n})
                    else:
                        m="your session has expired please login again"
                        return render(request,"home.html",{'m':m})
               else :
                    request.session['ss']=emailid
                    if 'ss' in request.session:
                        return render(request,"indexpatient.html",{'n':n})
                    else:
                        m="your session has expired please login again"
                        return render(request,"home.html",{'m':m})
                        
                     
        elif len(p)>0:  
            print(emailid)
            print("hi")        
            if password==p[0].P_H_password:
               a = hospital.objects.raw("select * from service_hospital where H_email = %s",[emailid])
               print(a)
               print(a[0].H_email)
               print(a[0].H_no_n_rooms)
               today = date.today()
               today=str(today)
               #current_time = time.strftime("%H:%M")
               b = appointment.objects.raw("select * from service_appointment where hosp_email=%s",[emailid])
               c = appointment.objects.raw("select id,count(p_email) from service_appointment where date = %s and hosp_email=%s",[today],[emailid])
               d = appointment.objects.raw("select id,count(p_email) from service_appointment where  hosp_email=%s",[emailid])
               print(len(b))
               print("\n\n\n")
               if len(b)==0:
                   pass
            #    else:
                #    abc=[]
                #    f=doctor.objects.raw("select D_email from service_doctor where D_hospitalemail=%s",[emailid])
                #    for i in range(len(f)):
                #       abc.append(appointment.objects.raw("select * from service_appointment where date = %s and hosp_email=%s Doctor_email=%s",[today],[emailid]),[[f[i].Doctor_email]])
                   
                   
                #    e=[]
                #    for i in range(len(f)):
                #       e.append(appointment.objects.raw("select * from service_appointment where date = %s and hosp_email=%s Doctor_email=%s ",[today],[emailid],[f[i].Doctor_email]))
                      
                #    now=datetime.now()
                #    ct=now.strftime("%H:%M")
                #    ct=ct.split(":");
                #    for i in range(len(ct)):
                #         ct[i]=int(ct[i]);
                #    time=ct[0]*60+ct[1]
                #    lst1=[]
                #    lst2=[]
                #    for i in range(len(f)):
                #        lst1.append(appointment.objects.raw("select id,timein from service_appointment where  hosp_email=%s and Doctor_email=%s date=%s",[emailid],[f[i].Doctor_email],[today]))
                #        lst2.append(appointment.objects.raw("select id,timeout from service_appointment where  hosp_email=%s and Doctor_email=%s ",[emailid],[f[i].Doctor_email],[today]))
                       
                #    w=[]
                #    q=[]
                #    r=[]
                #    s=[]
                #    for i in len(lst1):
                #        for j in len(lst1[i]):
                #            x=lst1[i][j].tiemin.split(":")
                #            y=lst2[i][j].timeout.split(":")
                #            x[0]=int(x[0])
                #            x[1]=int(x[1])
                #            y[0]=int(y[0])
                #            y[1]=int(y[1])
                #            r.append(x)
                #            s.append(y)
                           
                #        w.append(c)
                #        q.append(d)
                #    e=[]
                #    f=[]
                #    g=[]
                #    h=[]
                #    for i in range(len(lst1)):
                #        for j in range(len(lst1[i])):
                #            e.append((w[i][j][0]*60)+w[i][j][1])
                #            f.append((q[i][j][0]*60)+q[i][j][1])
                       
                #        g.append(e)
                #        h.append(f)
                #    k=[]    
                #    l=[]
                #    for i in range(len(g)):
                #        for j in range(len(g[i])):
                #            if time>g[i][j] and time<h[i][j]:
                #                k.append(j)
                #        l.append[k]
                        
                           
                           
        

            #    now=datetime.now()
            #    ct=now.strftime("%H:%M")
            #    ct=ct.split(":");
            #    for i in range(len(ct)):
            #       ct[i]=int(ct[i]);
            #    time=ct[0]*60+ct[1]
            # #    print(time)
            
            # #    lst1=["19:20","19:31","19:41","19:51"]
            # #    lst2=["19:30","19:40","19:50","20:00"]
            #    lst1=appointment.objects.raw("select id, timein from service_appointment where  hosp_email=%s",[emailid])
            #    lst2=appointment.objects.raw("select id, timeout from service_appointment where  hosp_email=%s",[emailid])
            #    a=[];
            #    b=[];
            #    for i in range(len(lst1)):
            #        x=lst1[i].tiemin.split(":");
            #        y=lst2[i].timeout.split(":");
            #        x[0]=int(x[0])
            #        x[1]=int(x[1])
            #        y[0]=int(y[0])
            #        y[1]=int(y[1])
            #        a.append(x)
            #        b.append(y)
            #    c=[]
            #    d=[]
            #    for i in range(len(lst1)):
            #        c.append((a[i][0]*60)+a[i][1])
            #        d.append((b[i][0]*60)+b[i][1])
            #    for i in range(len(c)):
            #        if time>c[i] and time<d[i]:
            #            p=i
                       
               
              
               request.session['ss']=emailid
               if 'ss' in request.session:
                    
                    if a[0].H_no_n_rooms==None:    
                        return render(request,"hospitaledit.html",{'e':today})
                    elif len(b)==0:
                        print(a[0].H_no_n_rooms)
                        print("\n\n\n\n")
                        c=[{'count(p_email)': ''}]
                        d=[{'count(p_email)':''}]
                        abc=[]
                        return render(request,"hospitalindex.html",{'e':today} )
                    # ,{'abc':abc} 
                        # ,{'d':d}
                        # , {'a':a},{'c':c}
                    else:
                        return render(request,"hospitalindex.html",{'e':today})
                         # ,{'d':d}
               else:
                    m="your session has expired please login again"
                    return render(request,"home.html",{'m':m})
                    
                       
            else:
                n="incorrect emil or password"
                return render(request,"signin.html",{'n':n}) 
                
        else:
            n="no such emilid found"
            return render(request,"signin.html",{'n':n})





    
    
    
def signup(request):
    return render(request,"signup.html")

def forget(request):
    return render(request,"froget_emil_otp.html")


def login(request):
    j=0
    global log
    n=""
    if request.method=="POST":
        selectoption=request.POST.get('selectoption')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        global el
        global pro
        el = email
        password=request.POST.get('password')
        gender=request.POST.getlist('gender')
        log=login1(selectoption=selectoption,fname=fname,lname=lname,email=email,password=password,gender=gender)
        pro=profilepatient(fname=fname,lname=lname,email=email,gender=gender)
        emil =  login1.objects.raw("select id,email from service_login1")
        for i in emil:
            if i.email==el:
                j=j+1 
                # print(i.email)
        #print(j)   
        
        if j!=0 :
            print("hi")
            n="emilid already exist"
            return render(request,"signup.html",{'n':n})
        
        else:    
            otp(el)
            return render(request,"new form.html")
        

def otp(el):
    el=el
    print(el)
    n=''
    global OTP
    OTP = random.randint(11111,99999)
    send_mail(
        'OTP',
        "your login otp is " +str(OTP),
        'vydya.doctor@gmail.com',
        [el],
        
    )
    
def otpsignp(request):
    if request.method=="POST":
        otp=request.POST.get('otp')
        if otp==str(OTP):
            log.save()
            pro.save()
            
            n="login successful"
            return render(request,"home.html",{'n':n})
        else:
            n='OTP incorrect'
            return render(request,"new form.html",{'n':n})
        
emailid=""      

def forget_email_otp(request):
    global emailid
    n=""
    if request.method=="POST": 
        emailid=request.POST.get('email')
        print(emailid)
        emil =  login1.objects.raw("select * from service_login1 where email = %s",[emailid])
        if len(emil)==0:
            n="no such emailid found"
            return render(request,"froget_emil_otp.html",{'n':n})
        else:
           otp(emailid)
           return render(request,"forget_p_otp.html")

def forget_p_otp(request):
    n=""
    if request.method=="POST":
        otp=request.POST.get('otp')
        pas=request.POST.get('password')
    if otp==str(OTP):
        log=connection.cursor()
        log.execute("UPDATE service_login1 SET password = %s WHERE email= %s",(pas, emailid))
        n="password updated successfully"
        return render(request,"home.html",{'n':n})
    else:
        n="incorrect otp"
        return render(request,"forget_p_otp.html",{'n':n})
        
        
    
        
        
        
               
        
def query(request):
    i=0
    a='raghavaganesh9@gmail.com'
    #emil = login1.objects.raw("select id,email from service_login1 where email= %s", [a])
    #emil = login1.objects.raw("select id,email from service_login1 where email='raghavaganesh9@gmail.com' ")
    emil =  login1.objects.raw("select id,email from service_login1")
    # print(emil.id)
    # print(emil.password)
    for i in emil:
       print(i.email)
       
    print(emil[0].email)
    
   
    return render(request,"query.html",{'email':emil[0].email})

            


    