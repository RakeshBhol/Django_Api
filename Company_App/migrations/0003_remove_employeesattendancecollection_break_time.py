# Generated by Django 3.1.1 on 2020-09-30 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company_App', '0002_auto_20200930_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeesattendancecollection',
            name='break_time',
        ),
    ]
