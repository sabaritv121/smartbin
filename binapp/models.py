from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_driver=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)

class driver(models.Model):
        user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='driver')
        name = models.CharField(max_length=50)
        Age = models.CharField(max_length=20, blank=True, null=True)
        Address = models.TextField(max_length=100)
        Phone_no = models.CharField(max_length=20)
        licence_no = models.CharField(max_length=20)
        whatsapp_no = models.CharField(max_length=20)
        Email = models.EmailField()
        Badge_no = models.CharField(max_length=20)
        approval_status=models.BooleanField(default=0)


        def __str__(self):
            return self.name

class Customer(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='user')
    Name = models.CharField(max_length=50)
    Contact_no = models.CharField(max_length=20)
    Email = models.EmailField()
    Address = models.TextField(max_length=100)
    approval_status = models.BooleanField(default=0)
    status = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.Name

class complaint(models.Model):
    user=models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    Complaint=models.TextField()
    date=models.DateField(auto_now=True)
    reply=models.TextField(null=True,blank=True)
    status = models.BooleanField(default=False, null=True)


class Complaintdriver(models.Model):
    user=models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    Complaint=models.TextField()
    date=models.DateField(auto_now=True)
    reply=models.TextField(null=True,blank=True)
    status = models.BooleanField(default=False, null=True)


class Notification(models.Model):
    notification=models.TextField()
    date=models.DateField(auto_now=True)





class Garbage(models.Model):
    date = models.DateTimeField(default=datetime.now)
    bin_name = models.CharField(max_length=20, null=True)
    location_latitude = models.CharField(max_length=20, unique=True, null=True)
    location_longitude = models.CharField(max_length=20, unique=True, null=True)
    status = models.CharField(max_length=15, null=True,blank=True)
    driver = models.ForeignKey(driver, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    status_d = models.BooleanField(default=False, null=True)



class Binrequest(models.Model):
    user=models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    request=models.TextField()
    location_latitude = models.CharField(max_length=20, unique=True, null=True)
    location_longitude = models.CharField(max_length=20, unique=True, null=True)
    date=models.DateField(auto_now=True)
    approval_status = models.BooleanField(default=False)
    status = models.BooleanField(default=False, null=True)