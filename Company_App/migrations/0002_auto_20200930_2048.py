# Generated by Django 3.1.1 on 2020-09-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='no_of_employee',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_phone_no',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone_no',
            field=models.PositiveIntegerField(null=True),
        ),
    ]