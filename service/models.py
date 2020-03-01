from django.db import models
from django.contrib.auth.models import User


class FTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ftp_user')
    host = models.CharField(max_length=50,null=True,verbose_name='Host')
    username = models.CharField(max_length=50,null=True,verbose_name='Username')
    password = models.CharField(max_length=50,null=True,verbose_name='Password')
    port = models.IntegerField(null=True,verbose_name='Port')

    def __str__(self):
        return self.username


class SSH(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ssh_user')
    host = models.CharField(max_length=50,null=True,verbose_name='Host')
    username = models.CharField(max_length=50,null=True,verbose_name='Username')
    password = models.CharField(max_length=50,null=True,verbose_name='Password')
    port = models.IntegerField(null=True,verbose_name='Port')

    def __str__(self):
        return self.username


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_user')
    url = models.CharField(max_length=100,null=True,verbose_name='Url')
    username = models.CharField(max_length=50,null=True,verbose_name='Username')
    password = models.CharField(max_length=50,null=True,verbose_name='Password')

    def __str__(self):
        return self.username


class Email(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_user')
    name = models.CharField(max_length=50,null=True,verbose_name='Name')
    username = models.CharField(max_length=50,null=True,verbose_name='Username')
    password = models.CharField(max_length=50,null=True,verbose_name='Password')

    def __str__(self):
        return self.username