import json
from urllib.request import urlopen

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from binapp.forms import LoginForm, UserForm, DriverForm, ComplaintForm, ComplaintdriverForm, NotificationForm, \
    SubscribeForm, garbage_form, RequsetForm

# garbage_form, SubscribeForm, RequsetForm
from binapp.models import driver, Customer, complaint, Complaintdriver, Notification, Garbage, Binrequest

####################################adminview#####################################################3
from smartbinclassifier import settings


def hello(request):
    return render(request,'welcome.html')

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        elif user is not None and user.is_customer:
            if user.user.approval_status == 1:
                login(request, user)
                return redirect('userhome')
            else:
                  messages.info(request, 'You are not Approved to login')
        elif user is not None and user.is_driver:
            if user.driver.approval_status==True:
                login(request, user)
                return redirect('driverhome')
            else:
                 messages.info(request, 'YOU ARE NOT APPROVED TO LOGIN')
    else:
            messages.info(request, 'invalid credentials')

    return render(request, 'login.html')


@login_required(login_url='login')
def adminhome(request):
    return render(request, 'admin/admin.html')


def dashboard(request):
    count = complaint.objects.filter(status=False)
    count1 = Complaintdriver.objects.filter(status=False)
    count2 = Binrequest.objects.filter(status=False)
    data = Garbage.objects.filter(status_d=False)
    total = len(data)
    return render(request, 'admin/dash1.html', {'count': len(count),
                                               'count1': len(count1),
                                               'count2': len(count2),
                                               'total': total})






@login_required(login_url='login')
def viewuser(request):
    c=Customer.objects.all()
    return render(request,'admin/viewuser.html',{'c':c})

@login_required(login_url='login')
def approve_user(request,id):
     c=Customer.objects.get(id=id)
     c.approval_status= True
     c.save()
     messages.info(request,'user approved successfully')
     return HttpResponseRedirect (reverse('viewuser'))
    # return render(request,'admin/viewuser.html')

# @login_required(login_url='login')
# def reject_user(request, id):
#     c = Customer.objects.get(id=id)
#     if request.method == 'POST':
#         c.approval_status = False
#         c.save()
#         messages.info(request, 'user rejection successfully')
#         return redirect('viewuser')
#     return render(request, 'admin/rejectuser.html')


def base(request):
    return render(request, 'base.html')


@login_required(login_url='login')
def viewcomplaint(request):
    comp=complaint.objects.all()
    return render(request,'admin/viewcomplaint.html',{'comp':comp})


@login_required(login_url='login')
def viewdrivercmp(request):
    drcomp=Complaintdriver.objects.all()
    return render(request,'admin/viewdrivercomplaintadmin.html',{'drcomp':drcomp})


@login_required(login_url='login')
def postuserreply(request,id):
    Reply=complaint.objects.get(id=id)
    if request.method == 'POST':
        r=request.POST.get('reply')
        Reply.reply = r
        Reply.save()
        messages.info(request,'Reply send')
        return redirect('viewcomplaint')
    return render(request,'admin/Replyuser.html',{'Reply':Reply})


@login_required(login_url='login')
def viewrequest(request):
    requ=Binrequest.objects.all()
    return render(request,'admin/viewbinrequest.html',{'requ':requ})

@login_required(login_url='login')
def postdriverreply(request,id):
    Rply=Complaintdriver.objects.get(id=id)
    print(Rply)
    if request.method == 'POST':
        r=request.POST.get('reply')
        Rply.reply = r
        Rply.save()
        messages.info(request,'Reply send')
        return redirect('viewdrivercmp')
    return render(request,'admin/Replydriver.html',{'Rply':Rply})

@login_required(login_url='login')
def postnotification(request):
    notifi=NotificationForm
    if request.method == 'POST':
        notifi = NotificationForm(request.POST)
        if notifi.is_valid():
            notifi.save()
            return redirect('admin_viewnotification')
    return render(request,'admin/postnotification.html',{'notifi':notifi})

@login_required(login_url='login')
def admin_viewnotification(request):
    noti=Notification.objects.all()
    return render(request,'admin/viewnotification.html',{'noti':noti})


@login_required(login_url='login')
def approve_driver(request, id):
    drive = driver.objects.get(id=id)
    drive.approval_status = True
    drive.save()
    messages.info(request, 'driver approved successfully')
    return HttpResponseRedirect(reverse('viewdriver'))


# @login_required(login_url='login')
# def reject_driver(request, id):
#     drive = driver.objects.get(id=id)
#     if request.method == 'POST':
#         drive.approval_status = False
#         drive.save()
#         messages.info(request, 'driver rejected successfully')
#         return redirect('admin/viewdriver')
#     return render(request, 'admin/rejectdriver.html')

@login_required(login_url='login')
def approve_birequest(request, id):
    bin= Binrequest.objects.get(id=id)
    bin.approval_status = True
    bin.save()
    messages.info(request, 'request approved successfully')
    return HttpResponseRedirect(reverse('viewrequest'))

@login_required(login_url='login')
def reject_binrequest(request, id):
    bin= Binrequest.objects.get(id=id)
    if request.method == 'POST':
        bin.approval_status = False
        bin.save()
        messages.info(request, 'request rejected successfully')
        return redirect('viewrequest')
    return render(request, 'admin/rejectrequest.html')


@login_required(login_url='login')
def viewdriver(request):
     d = driver.objects.all()
     return render(request, 'admin/viewdriver.html', {'d': d})



@login_required(login_url='login')
def add_bin(request):
    if request.method == 'POST':
        form = garbage_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminhome')
    else:
            form = garbage_form(request.POST)
    return render(request, 'admin/add-bin.html', {'form':form})


@login_required(login_url='login')
def garbage(request):

    data = Garbage.objects.all()
    return render(request, 'admin/garbageview.html', {'data': data})


@login_required(login_url='login')
def map_view1(request, id=None):
        data = Garbage.objects.get(id=id)
        return render(request, 'admin/map_view.html', {'data': data})

    # def viewbin(request):
    #     form = garbage_form()
    #     if request.method == 'POST':
    #         form = garbage_form(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             # messages.info(request,'Garbage Found')
    #             return redirect('garbage')
    #     return render(request, 'user/viewBin.html', {'form': form})









    #USER VIEWS
@login_required(login_url='login')
def userhome(request):
    return render(request,'user/userhome.html')



def registeruser(request):
    loginform = LoginForm()
    userform = UserForm()
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        userform = UserForm(request.POST)
        if loginform.is_valid() and userform.is_valid():
            user = loginform.save(commit=False)
            user.is_customer = True
            user.save()
            usr = userform.save(commit=False)
            usr.user = user
            usr.save()
            return redirect('login')
    return render(request, 'user/userregister.html', {'loginform': loginform, 'userform': userform})

@login_required(login_url='login')
def viewcmpuser(request):
    u=complaint.objects.filter(user=request.user)
    return render(request,'user/viewusercomplaint.html',{'u':u})


@login_required(login_url='login')
def postcomplaint(request):
    cmp=ComplaintForm
    u = request.user
    if request.method=='POST':
        cmp =ComplaintForm(request.POST)
        if cmp.is_valid() :
           obj= cmp.save(commit=False)
           obj.user= u
           obj.save()
           messages.info(request,"Complaint registered.....")
           return  redirect('userhome')
    else:
            cmp=ComplaintForm()
    return render(request,'user/postcomplaint.html',{'cmp':cmp})


@login_required(login_url='login')
def viewrequeststs(request):
    rests=Binrequest.objects.filter(user=request.user)
    return render(request,'user/viewrequeststs.html',{'rests':rests})

@login_required(login_url='login')
def postrequest(request):
    req=RequsetForm
    u = request.user
    if request.method=='POST':
        req =RequsetForm(request.POST)
        if req.is_valid() :
           obj= req.save(commit=False)
           obj.user= u
           obj.save()
           messages.info(request,"request registered.....")
           return redirect('viewrequeststs')
    return render(request,'user/postrequsetbin.html',{'req':req})


@login_required(login_url='login')
def viewnotification(request):
    noti=Notification.objects.all()
    return render(request,'user/viewnotification.html',{'noti':noti})





    #DRIVERVIEW
@login_required(login_url='login')
def driverhome(request):
    return render(request, 'driver/driverhome.html')


def registerdriver(request):
    loginform = LoginForm()
    driverform = DriverForm()
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        driverform = DriverForm(request.POST)
        if loginform.is_valid() and driverform.is_valid():
            user = loginform.save(commit=False)
            user.is_driver = True
            user.save()
            usr = driverform.save(commit=False)
            usr.user = user
            usr.save()
            return redirect('login')
    return render(request,'driver/driverregister.html', {'loginform': loginform, 'driverform': driverform})

@login_required(login_url='login')
def postdrivercomplaint(request):
    dcmp=ComplaintdriverForm
    u = request.user
    if request.method=='POST':
        dcmp =ComplaintdriverForm(request.POST)
        if dcmp.is_valid() :
           obj= dcmp.save(commit=False)
           obj.user= u
           obj.save()
           messages.info(request,"Complaint registered.....")
           return  redirect('driverhome')
    else:
            dcmp=ComplaintdriverForm()
    return render(request,'driver/postdrivercomplaint.html',{'dcmp':dcmp})

@login_required(login_url='login')
def viewdrivercomplaint(request):
    dcomp=Complaintdriver.objects.filter(user=request.user)
    return render(request,'driver/viewdrivercomplaint.html',{'dcomp':dcomp})


def notification(request):
    d=Notification.objects.all()
    return render(request,'driver/notification.html',{'d':d})


@login_required(login_url='login')
def garbage_userview(request):
    data = Garbage.objects.all()
    return render(request, 'driver/user_garbageview.html', {'data': data})



READ_API_KEY = 'E3F84Q8H2YL6TPB7'
CHANNEL_ID = '1771037'
@login_required(login_url='login')
def iotdata(request):

    while True:
        TS = urlopen(
            "https://api.thingspeak.com/channels/1771037/feeds.json?api_key=E3F84Q8H2YL6TPB7&results=2".format(CHANNEL_ID,
                                                                                                               READ_API_KEY))

        response = TS.read()

        data = json.loads(response.decode('utf-8'))

        print(data)

        print(data["feeds"][1]["field1"])


        a = data["feeds"][1]["field1"]
        b = data['channel']['latitude']
        c = data['channel']['longitude']
        print(a)
        print(b)
        print(c)
        return render(request,'admin/tst.html', {'a': a,'b':b,'c':c})




# def viewuserprof(request):
#     upro=Customer.objects.filter()
#     return render(request,'userprofile.html',{'upro':upro})
#


# from datetime import datetime
# from typing import List
#
#
# class Channel:
#     id: int
#     name: str
#     description: str
#     latitude: str
#     longitude: str
#     field1: str
#     created_at: datetime
#     updated_at: datetime
#     last_entry_id: int
#
#     def __init__(self, id: int, name: str, description: str, latitude: str, longitude: str, field1: str, created_at: datetime, updated_at: datetime, last_entry_id: int) -> None:
#         self.id = id
#         self.name = name
#         self.description = description
#         self.latitude = latitude
#         self.longitude = longitude
#         self.field1 = field1
#         self.created_at = created_at
#         self.updated_at = updated_at
#         self.last_entry_id = last_entry_id
#

# class Feed:
#     created_at: datetime
#     entry_id: int
#     field1: str
#
#     def __init__(self, created_at: datetime, entry_id: int, field1: str) -> None:
#         self.created_at = created_at
#         self.entry_id = entry_id
#         self.field1 = field1
#
#
# class Welcome1:
#     channel: Channel
#     feeds: List[Feed]
#
#     def __init__(self, channel: Channel, feeds: List[Feed]) -> None:
#         self.channel = channel
#         self.feeds = feeds




# class Channel:
#     id: int
#     name: str
#     description: str
#     latitude: str
#     longitude: str
#     field1: str
#     created_at: datetime
#     updated_at: datetime
#     last_entry_id: int
#
#     def __init__(self, id: int, name: str, description: str, latitude: str, longitude: str, field1: str, created_at: datetime, updated_at: datetime, last_entry_id: int) -> None:
#         self.id = id
#         self.name = name
#         self.description = description
#         self.latitude = latitude
#         self.longitude = longitude
#         self.field1 = field1
#         self.created_at = created_at
#         self.updated_at = updated_at
#         self.last_entry_id = last_entry_id
#
#
# class Feed:
#     created_at: datetime
#     entry_id: int
#     field1: str
#
#     def __init__(self, created_at: datetime, entry_id: int, field1: str) -> None:
#         self.created_at = created_at
#         self.entry_id = entry_id
#         self.field1 = field1
#
#
# class Welcome1:
#     channel: Channel
#     feeds: List[Feed]
#
#     def __init__(self, channel: Channel, feeds: List[Feed]) -> None:
#         self.channel = channel
#         self.feeds = feeds


@login_required(login_url='login')
def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'alert'
            message = 'bin filled....please clear the wastebin urgently'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Email send succesfully!')
            return redirect('subscribe')
    return render(request, 'gmail.html', {'form': form})


READ_API_KEY = 'E3F84Q8H2YL6TPB7'
CHANNEL_ID = '1771037'

@login_required(login_url='login')
def driver_iotdata(request):

    while True:
        TS = urlopen(
            "https://api.thingspeak.com/channels/1771037/feeds.json?api_key=E3F84Q8H2YL6TPB7&results=2".format(CHANNEL_ID,
                                                                                                               READ_API_KEY))

        response = TS.read()

        data = json.loads(response.decode('utf-8'))

        print(data)

        print(data["feeds"][1]["field1"])


        a = data["feeds"][1]["field1"]
        b = data['channel']['latitude']
        c = data['channel']['longitude']
        print(a)
        print(b)
        print(c)
        return render(request,'driver/test1.html', {'a': a,'b':b,'c':c})



def logout_view(request):
    logout(request)
    return redirect('login')
