# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-24 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0004_remove_purchaseorderline_network_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorderline',
            name='network_id',
            field=models.CharField(blank=True, max_length=240, null=True, verbose_name='Network ID'),
        ),
    ]