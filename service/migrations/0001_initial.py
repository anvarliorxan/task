# Generated by Django 2.1.5 on 2020-03-01 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, null=True, verbose_name='Url')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='Username')),
                ('password', models.CharField(max_length=50, null=True, verbose_name='Password')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='Username')),
                ('password', models.CharField(max_length=50, null=True, verbose_name='Password')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=50, null=True, verbose_name='Host')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='Username')),
                ('password', models.CharField(max_length=50, null=True, verbose_name='Password')),
                ('port', models.IntegerField(null=True, verbose_name='Port')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ftp_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SSH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=50, null=True, verbose_name='Host')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='Username')),
                ('password', models.CharField(max_length=50, null=True, verbose_name='Password')),
                ('port', models.IntegerField(null=True, verbose_name='Port')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ssh_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]