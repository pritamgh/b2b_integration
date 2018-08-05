# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 20:08
from __future__ import unicode_literals

import apps.users.models
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(blank=True, editable=False, null=True, upload_to=apps.users.models.upload_user_media_to),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(blank=True, help_text='Any User is Blocked/Unblocked by Buyer', max_length=100, null=True, verbose_name='User Status'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_role',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Role of User'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, help_text='Display username', max_length=255, null=True, verbose_name='Username'),
        ),
    ]
