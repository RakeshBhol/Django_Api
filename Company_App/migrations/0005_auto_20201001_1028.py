# Generated by Django 3.1.1 on 2020-10-01 04:58

import Company_App.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_App', '0004_auto_20201001_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='e_phone_no',
            field=models.CharField(max_length=10, null=True, validators=[Company_App.models.validate_phone]),
        ),
    ]
