# Generated by Django 3.0.5 on 2020-07-31 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0015_auto_20200731_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='description',
            name='fileurl',
        ),
    ]
