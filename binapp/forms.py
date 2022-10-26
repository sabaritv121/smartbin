from django import forms
from django.contrib.auth.forms import UserCreationForm

from binapp.models import Login, Customer, driver, complaint, Complaintdriver, Notification, Garbage, Binrequest


class LoginForm(UserCreationForm):
    username= forms.CharField(label='username')
    password1= forms.CharField(widget=forms.PasswordInput,label='password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='ConfirmPassword')
    class Meta:
        model=Login
        fields=('username','password1','password2')


class UserForm(forms.ModelForm):
    class Meta:
        model=Customer
        exclude = ('user','approval_status','status')

class DriverForm(forms.ModelForm):
    class Meta:
        model=driver
        exclude = ('user','approval_status')

class ComplaintForm(forms.ModelForm):
    class Meta:
        model=complaint
        exclude =('user','reply','status')

class ComplaintdriverForm(forms.ModelForm):
    class Meta:
        model=Complaintdriver
        exclude =('user','reply','status')

class NotificationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields=('notification',)


class RequsetForm(forms.ModelForm):
    class Meta:
        model=Binrequest
        fields=('request','location_latitude','location_longitude')

class garbage_form(forms.ModelForm):

    class Meta:
        model = Garbage
        fields = ('bin_name', 'location_latitude', 'location_longitude','driver','customer')



class SubscribeForm(forms.Form):
    email = forms.EmailField()

