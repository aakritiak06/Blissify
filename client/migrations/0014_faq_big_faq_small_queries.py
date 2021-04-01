# Generated by Django 3.0.5 on 2020-07-31 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_auto_20200727_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ_big',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='-')),
                ('content', models.TextField(default='-')),
                ('picture', models.FileField(blank=True, null=True, upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ_small',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='-')),
                ('content', models.TextField(default='-')),
            ],
        ),
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='-')),
                ('brief', models.TextField(default='-')),
            ],
        ),
    ]