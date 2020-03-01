from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import FTP,SSH,Email,Admin
from .forms import ftpForm,sshForm,emailForm,adminForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import logging


logger = logging.getLogger(__name__)



@login_required(login_url ="user:login")
def index(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        myftp = FTP.objects.filter(user = request.user,username__contains =keyword)
        myssh = SSH.objects.filter(user = request.user,username__contains =keyword)
        myadmin = Admin.objects.filter(user = request.user,username__contains =keyword)
        myemail = Email.objects.filter(user = request.user,username__contains =keyword)
        context ={
            'myftp':myftp,
            'myssh':myssh,
            'myadmin':myadmin,
            'myemail':myemail,
        }
        return render(request,'index.html',context)
    return render(request,'index.html')

@login_required(login_url ="user:login")
def addFtp(request):
    form = ftpForm(request.POST or None)
    if form.is_valid():
        ftp = form.save(commit=False)
        ftp.user = request.user
        ftp.save()
        messages.success(request,'Ftp parol yaratdiniz',)
        logger.info('Ftp parol elave olundu')
        to_mail = request.user.email
        send_mail(
        'Password Service',
        'Ftp parol ugurla əlavə olundu',    
        'testtask12345@gmail.com',
        [to_mail],
        fail_silently=False,
        )
        return redirect('service:myftp')
    return render(request,'service/addftp.html',{'form':form})

@login_required(login_url ="user:login")
def addSsh(request):
    form = sshForm(request.POST or None)
    if form.is_valid():
        ssh = form.save(commit=False)
        ssh.user = request.user
        ssh.save()
        messages.success(request,'Ssh parol yaratdiniz')
        logger.info('Ssh parol elave olundu')
        to_mail = request.user.email
        send_mail(
        'Password Service',
        'Ssh parol ugurla əlavə olundu',
        'testtask12345@gmail.com',
        [to_mail],
        fail_silently=False,
        )
        return redirect('service:myssh')
    return render(request,'service/addssh.html',{'form':form})

@login_required(login_url ="user:login")
def addAdmin(request):
    form = adminForm(request.POST or None)
    if form.is_valid():
        admin = form.save(commit=False)
        admin.user = request.user
        admin.save()
        messages.success(request,'Admin parol yaratdiniz')
        logger.info('Admin parol elave olundu')
        to_mail = request.user.email
        send_mail(
        'Password Service',
        'Admin parol ugurla əlavə olundu',
        'testtask12345@gmail.com',
        [to_mail],
        fail_silently=False,
        )
        return redirect('service:myadmin')
    return render(request,'service/addadmin.html',{'form':form})

@login_required(login_url ="user:login")
def addEmail(request):
    form = emailForm(request.POST or None)
    if form.is_valid():
        email = form.save(commit=False)
        email.user = request.user
        email.save()
        messages.success(request,'Email parol yaratdiniz')
        logger.info('Email parol elave olundu')
        to_mail = request.user.email
        send_mail(
        'Password Service',
        'Email parol ugurla əlavə olundu',
        'testtask12345@gmail.com',
        [to_mail],
        fail_silently=False,
        )
        return redirect('service:myemail')
    return render(request,'service/addemail.html',{'form':form})


def deleteFtp(request,id):
    delFtp = get_object_or_404(FTP,id= id,user= request.user)
    delFtp.delete()
    messages.success(request,'Ftp Password silinmisdir')
    logger.info('Ftp parol silindi')
    to_mail = request.user.email
    send_mail(
    'Password Service',
    'Ftp parolunuz silinmişdir',
    'testtask12345@gmail.com',
    [to_mail],
    fail_silently=False,
    )
    user = request.user
    return redirect('service:myftp')

def deleteSsh(request,id):
    delSsh = get_object_or_404(SSH,id= id,user= request.user)
    delSsh.delete()
    messages.success(request,'Ssh Password silinmisdir')
    logger.info('Ssh parol silindi')
    to_mail = request.user.email
    send_mail(
    'Password Service',
    'Ssh parolunuz silinmişdir',
    'testtask12345@gmail.com',
    [to_mail],
    fail_silently=False,
    )
    return redirect('service:myssh')

def deleteAdmin(request,id):
    delAdmin = get_object_or_404(Admin,id= id,user= request.user)
    delAdmin.delete()
    messages.success(request,'Admin Password silinmisdir')
    logger.info('Admin parol silindi')
    to_mail = request.user.email
    send_mail(
    'Password Service',
    'Admin parolunuz silinmişdir',
    'testtask12345@gmail.com',
    [to_mail],
    fail_silently=False,
    )
    logger.info('Admin parol silindi')
    return redirect('service:myadmin')

def deleteEmail(request,id):
    delEmail = get_object_or_404(Email,id= id,user= request.user)
    delEmail.delete()
    messages.success(request,'Email Password silinmisdir')
    logger.info('Email parol silindi')
    to_mail = request.user.email
    send_mail(
    'Password Service',
    'Email parolunuz silinmişdir',
    'testtask12345@gmail.com',
    [to_mail],
    fail_silently=False,
    )    
    return redirect('service:myemail')



def myFtp(request):
    myftp = FTP.objects.filter(user= request.user)
    return render(request,'service/myftp.html',{'myftp':myftp})

def mySsh(request):
    myssh = SSH.objects.filter(user= request.user)
    return render(request,'service/myssh.html',{'myssh':myssh})

def myAdmin(request):
    myadmin = Admin.objects.filter(user= request.user)
    return render(request,'service/myadmin.html',{'myadmin':myadmin})

def myEmail(request):
    myemail = Email.objects.filter(user= request.user)
    return render(request,'service/myemail.html',{'myemail':myemail})


@login_required(login_url ="user:login")
def editFtp(request,id):
    ftp = get_object_or_404(FTP,id= id,user= request.user)
    form = ftpForm(request.POST or None,instance =ftp)
    if request.method == 'POST':
        if form.is_valid():
            ftp = form.save(commit=False)
            ftp.user = request.user
            ftp.save()
            messages.success(request,'Ftp parolunuz deyisdirildi')
            logger.info('Ftp parol deyisdirildi')
            to_mail = request.user.email
            send_mail(
            'Password Service',
            'Ftp parolunuzda dəyişiklik olundu',
            'testtask12345@gmail.com',
            [to_mail],
            fail_silently=False,
            )
            return redirect('service:myftp')
    return render(request,'service/edit_ftp.html',{'form':form})


@login_required(login_url ="user:login")
def editSsh(request,id):
    ssh = get_object_or_404(SSH,id= id,user= request.user)
    form = sshForm(request.POST or None,instance =ssh)
    if request.method == 'POST':
        if form.is_valid():
            ssh = form.save(commit=False)
            ssh.user = request.user
            ssh.save()
            messages.success(request,'Ssh parolunuz deyisdirildi')
            logger.info('Ssh parol deyisdirildi')
            to_mail = request.user.email
            send_mail(
            'Password Service',
            'Ssh parolunuzda dəyişiklik oldu',
            'testtask12345@gmail.com',
            [to_mail],
            fail_silently=False,
            )
            return redirect('service:myssh')
    return render(request,'service/edit_ssh.html',{'form':form})


@login_required(login_url ="user:login")
def editAdmin(request,id):
    admin = get_object_or_404(Admin,id= id,user= request.user)
    form = adminForm(request.POST or None,instance =admin)
    if request.method == 'POST':
        if form.is_valid():
            admin = form.save(commit=False)
            admin.user = request.user
            admin.save()
            messages.success(request,'Admin parolunuz deyisdirildi')
            logger.info('Admin parol deyisdirildi')
            to_mail = request.user.email
            send_mail(
            'Password Service',
            'Admin parolunuzda dəyişiklik oldu',
            'testtask12345@gmail.com',
            [to_mail],
            fail_silently=False,
            )
            return redirect('service:myadmin')
    return render(request,'service/edit_admin.html',{'form':form})


@login_required(login_url ="user:login")
def editEmail(request,id):
    email = get_object_or_404(Email,id= id,user= request.user)
    form = emailForm(request.POST or None,instance =email)
    if request.method == 'POST':
        if form.is_valid():
            email = form.save(commit=False)
            email.user = request.user
            email.save()
            messages.success(request,'Email parolunuz deyisdirildi')
            logger.info('Email parol deyisdirildi')
            to_mail = request.user.email
            send_mail(
            'Password Service',
            'Email parolunuzda dəyişiklik oldu',
            'testtask12345@gmail.com',
            [to_mail],
            fail_silently=False,
            )            
            return redirect('service:myemail')
    return render(request,'service/edit_email.html',{'form':form})


