from django.urls import path
from .import views

app_name = 'service'

urlpatterns = [
    path('addftp/',views.addFtp,name='addftp'),
    path('addssh/',views.addSsh,name='addssh'),
    path('addadmin/',views.addAdmin,name='addadmin'),
    path('addemail/',views.addEmail,name='addemail'),

    path('deleteftp/<str:id>',views.deleteFtp,name='deleteftp'),
    path('deletessh/<str:id>',views.deleteSsh,name='deletessh'),
    path('deleteadmin/<str:id>',views.deleteAdmin,name='deleteadmin'),
    path('deleteemail/<str:id>',views.deleteEmail,name='deleteemail'),
    
    path('myftp/',views.myFtp,name='myftp'),
    path('myssh/',views.mySsh,name='myssh'),
    path('myadmin/',views.myAdmin,name='myadmin'),
    path('myemail/',views.myEmail,name='myemail'),

    path('editftp/<str:id>',views.editFtp,name='editftp'),
    path('editssh/<str:id>',views.editSsh,name='editssh'),
    path('editadmin/<str:id>',views.editAdmin,name='editadmin'),
    path('editemail/<str:id>',views.editEmail,name='editemail'),


]       