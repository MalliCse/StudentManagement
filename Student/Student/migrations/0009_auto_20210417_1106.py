# Generated by Django 3.1.7 on 2021-04-17 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0008_auto_20210417_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='Paid',
        ),
        migrations.RemoveField(
            model_name='register',
            name='address',
        ),
        migrations.RemoveField(
            model_name='register',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='register',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
        migrations.RemoveField(
            model_name='register',
            name='total_fee',
        ),
    ]
