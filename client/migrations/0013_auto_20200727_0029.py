# Generated by Django 3.0.5 on 2020-07-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_problem_reports'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picname',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='post',
            name='picurl',
            field=models.TextField(default='-'),
        ),
    ]