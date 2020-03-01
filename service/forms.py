from django import forms
from .models import Admin,Email,FTP,SSH

class ftpForm(forms.ModelForm):
    password = forms.CharField(max_length=40,label = 'Password',widget=forms.PasswordInput)
    class Meta:
        model= FTP
        fields = ['host','username','password','port',]

class sshForm(forms.ModelForm):
    password = forms.CharField(max_length=40,label = 'Password',widget=forms.PasswordInput)
    class Meta:
        model= SSH
        fields = ['host','username','password','port',]
        
class adminForm(forms.ModelForm):
    password = forms.CharField(max_length=40,label = 'Password',widget=forms.PasswordInput)
    class Meta:
        model = Admin

        fields = ['url','username','password',]


class emailForm(forms.ModelForm):
    password = forms.CharField(max_length=40,label = 'Password',widget=forms.PasswordInput)
    class Meta:
        model = Email
        fields = ['name','username','password']